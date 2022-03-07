import numpy as np
from querymain import gFile, gIndex,line_offset, fileData
import time
from linecache import getline
import nltk


def search(tokens: list):
    """
    :param tokens: list of query tokens from user input
    :return: a smaller dictionary with the tokens that were searched for with original values and a frequency dictionary
    of the query terms
    """
    # create a frequency dict of tokens in the given query
    freqDict = nltk.FreqDist(tokens)
    resultDict = {}
    for token in tokens:
        try:
            lineNum = line_offset[gIndex[token] - 1]
            # move to that position in the file
            gFile.seek(lineNum)
            info = gFile.readline().split()
            # gather posting list and add to a dictionary for later retrieval
            doc = info[0]
            postingList = info[1:]
            for i in range(len(postingList)):
                value = postingList[i]
                values = value.split(',')
                docID = int(values[0])
                tfidf = float(values[1])
                postingList[i] = (docID, tfidf)
            key = (doc, token)
            resultDict[key] = postingList
            # return to beginning of the file
            gFile.seek(0, 0)
        except KeyError as error:
            # this error means that this token could not be found in our overall index
            print(token, " could not be found.")
            resultDict.clear()
            return resultDict, freqDict
    return resultDict, freqDict


def cosineSimilarity(docDict: dict, freqDict: dict):
    """
    :param tokenDict: smaller dictionary with tokens user is searching for whose values is same as in the index
    :return: boolean matrix of tokens and documents, will be a 2D array
    Will parse through given dictionary, find all pages that the words go in and place a 1 wherever the documents
    appear
    """
    # find the number of total pages for all tokens and map them to an index
    pageMapping = {}
    indexCounter = 0
    for key in docDict:
        postingList = docDict[key]
        for post in postingList:
            docID = post[0]
            if docID not in pageMapping:
                pageMapping[docID] = indexCounter
                indexCounter += 1

    # create a boolean matrix that shows which terms are in which document
    matrixShape = (len(docDict), len(pageMapping))
    matrix = np.zeros(matrixShape)

    # maps which tokens belong in which row
    tokenMapping = {}
    i = 0
    # add the tfidf score for a document if that term is present
    for token in docDict:
        tokenMapping[token] = i
        postingList = docDict[token]
        for values in postingList:
            docID = values[0]
            tfidf = values[1]
            matrix[i, pageMapping[docID]] = tfidf
        i += 1

    # reverse the list to get the document number given the index
    pageMapping = {value: key for key, value in pageMapping.items()}

    # get all the documents that contain all of the terms in the query
    similarDocs = []
    for i in range(matrix.shape[1]):
        zeros = np.argwhere(matrix[:, i] > 0)
        if len(zeros) == matrix.shape[0]:
            similarDocs.append(i)

    # computing the cosine similarity between each term in the query and the documents
    scores = {}
    length = {}
    for token in docDict:
        word = token[1]
        postingList = docDict[token]
        numDocumentsWithTerm = len(postingList)
        # creating a tfidf weight for each query term
        weight = (1 + np.log(freqDict[word])) * (np.log(55393 / numDocumentsWithTerm))
        for doc in similarDocs:
            tfidf = matrix[tokenMapping[token], doc]
            docNum = pageMapping[doc]
            # computing the cosine similarity between term and document
            if docNum in scores:
                scores[docNum] += weight * tfidf
            else:
                scores[docNum] = weight * tfidf
            if docNum in length:
                length[docNum] += 1
            else:
                length[docNum] = 1

    # normalizing the scores
    for doc in scores:
        scores[doc] = scores[doc] / length[doc]

    return scores




def getTopK(scores: list):
    '''
    :param scores: takes in a list of tuples that contain a score and the document number
    :return: returns a final list of the top 20 highest scores
    '''
    final = []
    scores = [(key, value) for key, value in sorted(scores.items(), key=lambda a: a[1], reverse=True)]
    for kv in scores[:20]:
        doc = kv[0]
        final.append(fileData[str(doc)]['url'])
    return final
