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
    pass


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
    while len(listMostDesirable <= 5):
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


