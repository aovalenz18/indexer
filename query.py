import json
import numpy as np
from pathlib import Path
from querymain import gFile, gIndex


def search(tokens: list):
    # Kazeem
    """
    :param tokens: list of query tokens from user input
    :return: a smaller dictionary with the tokens that were searched for with original values
    """
    # Editing to gather information from the text file

    # indexFile = open("index.json")
    # fileData = json.load(indexFile)
    # resultDict = dict()
    #
    # for token in tokens:
    #     resultDict[token] = fileData[token]
    # return resultDict

    resultDict = {}
    for token in tokens:
        try:
            lineNum = gIndex[token]
            print(lineNum)
            # move to that position in the file
            gFile.seek(lineNum)
            info = gFile.readline().split()
            token = info[0]
            postingList = info[1:]
            for i in range(len(postingList)):
                value = postingList[i]
                values = value.split(',')
                docID = int(values[0])
                tfidf = float(values[1])
                postingList[i] = (docID, tfidf)

            resultDict[token] = postingList
            # return to beginning of the file
            gFile.seek(0, 0)
        except KeyError as error:
            print(token, " could not be found.")
    return resultDict


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
        postingList = tokenDict[key]
        for post in postingList:
            docID = post[0]
            if docID not in pageMapping:
                pageMapping[docID] = indexCounter
                indexCounter += 1

    matrixShape = (len(tokenDict), len(pageMapping))
    matrix = np.zeros(matrixShape)

    i = 0  # counter for each token in the dictionary
    for token in tokenDict:
        postingList = tokenDict[token]
        for values in postingList:
            docID = values[0]
            tfidf = values[1]
            matrix[i, pageMapping[docID]] = tfidf
        i += 1

    pageMapping = {value: key for key, value in pageMapping.items()}

    return matrix, pageMapping


def matrixResults(matrix: [list], pageMapping: dict):
    # Shaun
    '''
    :param matrix: boolean matrix that holds all occurences of token in a webpage
    :return: a list of top 5 documents where the words appear

    Go through matrix and find combination of values where the specified tokens appear,
    and navigate through dictionary to get the corresponding file path name
    '''

    for i in range(len(matrix)):
        tfidfSums = []
        sum = 0
        for j in range(len(matrix[0])):
            sum+=matrix[i][j]
        tfidfSums.append((pageMapping[i], sum))
    
    tupleList = sorted(tfidfSums, key=lambda x: (x[1]), reverse=True)[0:9]
    finalList = []
    for docs in tupleList:
        finalList.append(docs[0])
    return finalList

    '''
    listMostDesirable = []
    bestMatch = len(matrix)
    infLoop = 0
    while len(listMostDesirable) < 5:
        if infLoop == 8:
            break
        for i in range(len(matrix[0])):
            if len(listMostDesirable) < 5:
                incCount = 0
                for token in matrix:
                    if token[i] == 1:
                        incCount += 1
                if incCount == bestMatch:
                    listMostDesirable.append(pageMapping[i])
        bestMatch -= 1
        infLoop += 1

    with open("docIndex.json", "r+") as file:
        fileData = json.load(file)
        finalTop5 = []
        for docInd in listMostDesirable:
            finalTop5.append(fileData[docInd]['url'])'''
        
        
    return finalTop5