import numpy as np
import json

from clustering.training import TrainingModel

FILE_WITH_WEIGHTS = 'clustering/synapses_new.json'

# ERROR_THRESHOLD = 0.03
# load our calculated synapse values


def get_weights(filename):
    with open(filename) as data_file:
        synapse = json.load(data_file)
        synapse_0 = np.asarray(synapse['synapse0'])
        synapse_1 = np.asarray(synapse['synapse1'])
    return synapse_0, synapse_1, synapse


def classify(sentence, show_details, error_threshold):
    train_model = TrainingModel()
    synapse_0, synapse_1, _ = get_weights(filename=FILE_WITH_WEIGHTS)
    results = train_model.think(sentence, synapse_0, synapse_1, train_model.words, show_details)
    results = [[i, r] for i, r in enumerate(results) if r > error_threshold]
    results.sort(key=lambda x: x[1], reverse=True)
    return_results = [[train_model.classes[r[0]], r[1]] for r in results]
    return return_results


def correlation_coef(class_1, class_2):
    synapse_0, _, synapse = get_weights(filename=FILE_WITH_WEIGHTS)
    first_index = synapse['classes'].index(class_1)
    second_index = synapse['classes'].index(class_2)
    array_1 = [item[first_index] for item in synapse_0]
    array_2 = [item[second_index] for item in synapse_0]
    corrcoef = np.corrcoef(array_1, array_2)
    return corrcoef[0][1]

# i = 0
# for i in range(1000):
#     i += 0.0001
# print(classify('what is booger?', True, 0))

