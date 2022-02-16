import numpy as np


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
    pass

if __name__ == "__main__":

    adict = {"real": [
        {
            "9": [
                2
            ],
            "8": [
                2
            ]
        },
        0
    ],
    "time": [
        {
            "9": [
                2
            ],
            "1": [
                2
            ]
        },
        0
    ],
    "dre": [
        {
            "9": [
                2
            ],
            "4": [
                2
            ]
        },
        0
    ],
    "feedback": [
        {
            "9": [
                2
            ],
            "7": [
                2
            ]
        },
        0
    ],
    "if": [
        {
            "9": [
                2
            ],
            "5": [
                2
            ]
        },
        0
    ],}

    booleanMatrix = createMatrix(adict)
    print(booleanMatrix)