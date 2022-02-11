import json
import nltk

def createIndex(tokens: [str], html: int):
    """creates the index of all tokens with list of postings
    JSON file structure:
    token: [ [html,frequency] ]
    keep appending to value list """

    # create a frequency dictionary for all the tokens
    freqDict = nltk.FreqDist(tokens)

    # first open indexer file and read its content
    with open('index.json', 'w+') as jsonFile:
        index = json.loads(jsonFile)
        # go through all tokens and add to the indexer
        for token in freqDict:
            postings = [{html: [0]}, 0]
            if token in index:
                # list of postings
                postings = index[token]
                # add key into document dictionary
                frequency = postings[0][html]
                updatedFrequency = frequency + 1
                postings[0][html][0] = updatedFrequency # this will have an updated list
            index[token] = postings
            # start from beginning of file
            jsonFile.seek(0)
            # add to jsonFile and
            json.dump(index, jsonFile)
            jsonFile.truncate()
