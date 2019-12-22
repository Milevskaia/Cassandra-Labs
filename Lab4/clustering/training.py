import datetime
import json
import numpy as np
import nltk
import time
from clustering.ext import stemmer
from clustering.preprocess_data import preprocessed_data
from load_dataset import training_data


class TrainingModel:
    def __init__(self):
        result = preprocessed_data(training_data())
        self.documents = result[0]
        self.classes = result[1]
        self.words = result[2]
        self.output = result[3]
        self.training = result[4]

    @staticmethod
    def sigmoid(x):
        output = 1 / (1 + np.exp(-x))
        return output

    # convert output of sigmoid function to its derivative
    @staticmethod
    def sigmoid_output_to_derivative(output):
        return output * (1 - output)

    @staticmethod
    def clean_up_sentence(sentence):
        # tokenize the pattern
        sentence_words = nltk.word_tokenize(sentence)
        # stem each word
        sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words

    # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
    def bow(self, sentence, words, show_details=False):
        # tokenize the pattern
        sentence_words = self.clean_up_sentence(sentence)
        # bag of words
        bag = [0] * len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print("found in bag: %s" % w)

        return (np.array(bag))

    def think(self, sentence, synapse_0, synapse_1, words, show_details=False):
        x = self.bow(sentence.lower(), words, show_details)
        if show_details:
            print("sentence:", sentence, "\n bow:", x)
        # input layer is our bag of words
        l0 = x
        # matrix multiplication of input and hidden layer
        l1 = self.sigmoid(np.dot(l0, synapse_0))
        # output layer
        l2 = self.sigmoid(np.dot(l1, synapse_1))
        return l2

    def train(self, X, y, hidden_neurons=100, alpha=10.0, epochs=100000, dropout=False, dropout_percent=0.5):
        print("Training with {} neurons, alpha:{}, dropout:{} {}".format(hidden_neurons, str(alpha), dropout, dropout_percent if dropout else ''))
        print("Input matrix: {}x{}    Output matrix: {}x{}".format(len(X), len(X[0]), 1, len(classes)))
        np.random.seed(1)

        last_mean_error = 1
        # randomly initialize our weights with mean 0
        synapse_0 = 2 * np.random.random((len(X[0]), hidden_neurons)) - 1
        synapse_1 = 2 * np.random.random((hidden_neurons, len(classes))) - 1

        prev_synapse_0_weight_update = np.zeros_like(synapse_0)
        prev_synapse_1_weight_update = np.zeros_like(synapse_1)

        synapse_0_direction_count = np.zeros_like(synapse_0)
        synapse_1_direction_count = np.zeros_like(synapse_1)

        for j in iter(range(epochs + 1)):

            # Feed forward through layers 0, 1, and 2
            layer_0 = X
            layer_1 = self.sigmoid(np.dot(layer_0, synapse_0))

            if (dropout):
                layer_1 *= np.random.binomial([np.ones((len(X), hidden_neurons))], 1 - dropout_percent)[0] * (
                            1.0 / (1 - dropout_percent))

            layer_2 = self.sigmoid(np.dot(layer_1, synapse_1))

            # how much did we miss the target value?

            layer_2_error = y - layer_2

            if (j % 10000) == 0 and j > 5000:
                # if this 10k iteration's error is greater than the last iteration, break out
                if np.mean(np.abs(layer_2_error)) < last_mean_error:
                    print("delta after " + str(j) + " iterations:" + str(np.mean(np.abs(layer_2_error))))
                    last_mean_error = np.mean(np.abs(layer_2_error))
                else:
                    print("break:", np.mean(np.abs(layer_2_error)), ">", last_mean_error)
                    break

            # in what direction is the target value?
            # were we really sure? if so, don't change too much.
            layer_2_delta = layer_2_error * self.sigmoid_output_to_derivative(layer_2)

            # how much did each l1 value contribute to the l2 error (according to the weights)?
            layer_1_error = layer_2_delta.dot(synapse_1.T)

            # in what direction is the target l1?
            # were we really sure? if so, don't change too much.
            layer_1_delta = layer_1_error * self.sigmoid_output_to_derivative(layer_1)

            synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
            synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))

            if (j > 0):
                synapse_0_direction_count += np.abs(
                    ((synapse_0_weight_update > 0) + 0) - ((prev_synapse_0_weight_update > 0) + 0))
                synapse_1_direction_count += np.abs(
                    ((synapse_1_weight_update > 0) + 0) - ((prev_synapse_1_weight_update > 0) + 0))

            synapse_1 += alpha * synapse_1_weight_update
            synapse_0 += alpha * synapse_0_weight_update

            prev_synapse_0_weight_update = synapse_0_weight_update
            prev_synapse_1_weight_update = synapse_1_weight_update

        now = datetime.datetime.now()

        # persist synapses
        synapse = {'synapse0': synapse_0.tolist(), 'synapse1': synapse_1.tolist(),
                   'datetime': now.strftime("%Y-%m-%d %H:%M"),
                   'words': self.words,
                   'classes': self.classes
                   }
        synapse_file = "synapses_temp.json"

        with open(synapse_file, 'w') as outfile:
            json.dump(synapse, outfile, indent=4, sort_keys=True)
        print("saved synapses to:", synapse_file)


def start_train():
    train_model = TrainingModel()
    x = np.array(train_model.training)
    y = np.array(train_model.output)

    start_time = time.time()

    train_model.train(x, y, hidden_neurons=20, alpha=0.1, epochs=100000, dropout=False, dropout_percent=0.2)

    elapsed_time = time.time() - start_time
    print("processing time:", elapsed_time, "seconds")