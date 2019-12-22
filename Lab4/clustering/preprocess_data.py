import nltk

from clustering.ext import stemmer


def preprocessed_data(training_data):
    print('Start preprocessing data')
    words = []
    classes = []
    documents = []
    ignore_words = ['?']
    for pattern in training_data:
        w = nltk.word_tokenize(pattern['question'])
        words.extend(w)
        documents.append((w, pattern['discipline']))
        if pattern['discipline'] not in classes:
            classes.append(pattern['discipline'])

    # stem and lower each word and remove duplicates
    words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
    words = list(set(words))

    # remove duplicates
    classes = list(set(classes))
    # create our training data
    training = []
    output = []
    # create an empty array for our output
    output_empty = [0] * len(classes)
    # training set, bag of words for each sentence
    i = 0
    for doc in documents:
        i += 1
        # initialize our bag of words
        bag = []
        # list of tokenized words for the pattern
        pattern_words = doc[0]
        # stem each word
        pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
        # create our bag of words array
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)

        training.append(bag)
        # output is a '0' for each tag and '1' for current tag
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        output.append(output_row)
        if i > 2000:
            return documents, classes, words, output, training
    return documents, classes, words, output, training




