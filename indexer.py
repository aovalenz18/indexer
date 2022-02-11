import json
import nltk
from main import globalIndex

def createIndex(tokens: [str], html: int):
    """creates the index of all tokens with list of postings
    JSON file structure:
    token: [ [html,frequency] ]
    keep appending to value list """

    # create a frequency dictionary for all the tokens
    freqDict = nltk.FreqDist(tokens)

    # go through all tokens and add to the global indexer
    for token in freqDict:
        postings = [{html: [freqDict[token]]}, 0]
        if token in globalIndex:
            # list of postings
            postings = globalIndex[token]
            # add key into document dictionary
            frequency = postings[0][html][0]
            updatedFrequency = frequency + freqDict[token]
            postings[0][html][0] = updatedFrequency # this will have an updated list
        globalIndex[token] = postings

    # if index is a multiple of 100, we dump into jsonFile and clear the global index
    if html % 100 == 0:
        with open('index.json', 'r+') as jsonFile:
            jsonFile.seek(0)
            # add to jsonFile and
            json.dump(globalIndex, jsonFile)
            jsonFile.truncate()
        globalIndex.clear()


