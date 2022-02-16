import numpy as np
from subprocess import list2cmdline
from typing import final


def search(tokens: list):
    # Kazeem
    """
    :param tokens: list of query tokens from user input
    :return: a smaller dictionary with the tokens that were searched for with original values
    """
    pass


def createMatrix(tokenDict: dict):
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
    for key in tokenDict:
        pages = tokenDict[key][0].keys()
        for page in pages:
            if page not in pageMapping:
                pageMapping[page] = indexCounter
                indexCounter += 1

    matrixShape = (len(tokenDict), len(pageMapping))
    matrix = np.zeros(matrixShape)

    i = 0 # counter for each token in the dictionary
    for token in tokenDict:
        pages = list(tokenDict[token][0].keys())
        for page in pages:
            matrix[i, pageMapping[page]] = 1
        i += 1

    return matrix


def matrixResults(matrix: [list], tokenDict: dict):
    # Shaun
    '''
    :param matrix: boolean matrix that holds all occurences of token in a webpage
    :return: a list of top 5 documents where the words appear

    Go through matrix and find combination of values where the specified tokens appear,
    and navigate through dictionary to get the corresponding file path name
    '''

    listMostDesirable = []
    bestMatch = len(matrix)
    infLoop = 0
    while len(listMostDesirable < 5):
        if infLoop == 8:
            break
        for i in range(len(matrix[0])):
            incCount = 0
            for token in matrix:
                if token[i] == 1:
                    incCount += 1
            if incCount == bestMatch:
                listMostDesirable.append(matrix[0][i])
        bestMatch-=1
        infLoop+=1
        
    return listMostDesirable


