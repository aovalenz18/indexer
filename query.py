import numpy as np
from querymain import gFile, gIndex,line_offset, fileData
import nltk
import pandas as pd


def search(tokens: list):
    # Kazeem
    """
    :param tokens: list of query tokens from user input
    :return: a smaller dictionary with the tokens that were searched for with original values
    """
    for token in tokens:
        try:
            lineNum = line_offset[gIndex[token] - 1]
            # move to that position in the file

            gFile.seek(lineNum)
            info = gFile.readline().split()
            #print(info)
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
            print(token, " could not be found.")
    return resultDict, freqDict


def createMatrix(docDict: dict, freqDict: dict):
    # Anthony
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

    matrixShape = (len(docDict), len(pageMapping))
    matrix = np.zeros(matrixShape)

    tokenMapping = {}
    i = 0  # counter for each token in the dictionary
    for token in docDict:
        tokenMapping[token] = i
        postingList = docDict[token]
        for values in postingList:
            docID = values[0]
            tfidf = values[1]
            matrix[i, pageMapping[docID]] = tfidf
        i += 1

    pageMapping = {value: key for key, value in pageMapping.items()}

    similarDocs = []
    for i in range(matrix.shape[1]):
        zeros = np.argwhere(matrix[:, i] > 0)
        if len(zeros) == matrix.shape[0]:
            similarDocs.append(i)

    scores = {}
    length = {}
    for token in docDict:
        word = token[1]
        postingList = docDict[token]
        # postingList = [(k, v) for k, v in postingList if k in similarDocs]
        numDocumentsWithTerm = len(postingList)
        weight = (1 + np.log(freqDict[word])) * (np.log(55393 / numDocumentsWithTerm))
        for doc in similarDocs:
            # docID = doc[1]
            tfidf = matrix[tokenMapping[token], doc]

            docNum = pageMapping[doc]
            if docNum in scores:
                scores[docNum] += weight * tfidf
            else:
                scores[docNum] = weight * tfidf
            if docNum in length:
                length[docNum] += 1
            else:
                length[docNum] = 1

    for doc in scores:
        scores[doc] = scores[doc] / length[doc]

    return scores



def getTopK(scores: dict):
    final = []
    scores = [(key, value) for key, value in sorted(scores.items(), key=lambda a: a[1], reverse=True)]
    for kv in scores[:20]:
        doc = kv[0]
        print(doc)
        final.append(fileData[str(doc)]['url'])
    return final
