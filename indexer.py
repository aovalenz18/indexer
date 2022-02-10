import json
import nltk

def createIndex(tokens, html):
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
            postings = [[html, 1]]
            if token in index:
                # list of postings
                postings = index[token]
                # go through list and find the right html page
                updatedFrequency = 0
                for posting in postings:
                    if posting[0] == html:
                        updatedFrequency = posting[1] + freqDict[token]
                        break
                # add this to list of postings
                data = [html, updatedFrequency]
                # update list of postings
                postings.append(data)

            index[token] = postings
            # start from beginning of file
            jsonFile.seek(0)
            # add to jsonFile and
            json.dump(index, jsonFile)
            jsonFile.truncate()
