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
    pass
