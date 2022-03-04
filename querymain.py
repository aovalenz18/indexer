from interface import *
from query import *
import json
import time


def openFiles():
    """
    :return: index dictionary and file index objects
    This function is going to open up the lineNums.json
    """
    with open('lineNums.json') as f:
        data = json.load(f)
    # this is going to contain the index of the tokens

    file = open("txtIndex.txt", "r")

    line_offset = []
    offset = 0
    for line in file:
        line_offset.append(offset)
        offset += len(line) + 1
    file.seek(0)

    return data, file, line_offset


gIndex, gFile, line_offset = openFiles()

with open("docIndex.json", "r+") as file:
    fileData = json.load(file)


def closeFile(file):
    file.close()


'''Main part of query program, have terminal interface to access indexer
Get user input and call outside functions to get the query results'''
if __name__ == "__main__":

    # gIndex, gFile = openFiles()

    print("Assignment #3 - Search Engine")
    userInput = getUserInput()

    while userInput != "q":
        # Start the search time
        startTime = int(time.time() * 1000)

        # Get a smaller dictionary from the indexer from the result of the userInput
        indexDict = search(userInput)

        for g in indexDict:
            print(g)
        endTime3 = int(time.time() * 1000)


        if len(indexDict) == 0:
            print("No results found with all words in a document.")
            endTime = int(time.time() * 1000)
        else:
            startTime1 = int(time.time() * 1000)
            # Create a matrix result from the indexDict
            matrix = createMatrix(indexDict)
            endTime1 = int(time.time() * 1000)

            startTime2 = int(time.time() * 1000)
            # Get the top 5 documents based on the matrix
            documentList = matrixResults(matrix[0], matrix[1])

            endTime = int(time.time() * 1000)

            # Output the documentList
            print("\nResult:\n")
            for i, list in zip(range(1, len(documentList)+1), documentList):
                print(str(i)+ " : "+ str(list))


        print("\nTotal time to search: " + str(endTime-startTime) + "ms\n")
        print("\nTotal time to search function: " + str(endTime3-startTime) + "ms\n")
        print("\nTotal time to createMatrix: " + str(endTime1-startTime1) + "ms\n")
        print("\nTotal time to matrixResult: " + str(endTime-startTime2) + "ms\n")

        userInput = getUserInput()

    closeFile(gFile)
    print("\nClosing the program")
