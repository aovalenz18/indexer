from interface import *
from query import *
import json
import time

gIndex = {}
gFile = None


def openFiles():
    """
    :return: index dictionary and file index objects
    This function is going to open up the lineNums.json
    """
    with open('data.json') as f:
        data = json.load(f)
    # this is going to contain the index of the tokens

    file = open("txtIndex.txt", "r")

    return data, file


def closeFile(file):
    file.close()

'''Main part of query program, have terminal interface to access indexer
Get user input and call outside functions to get the query results'''
if __name__ == "__main__":

    gIndex, gFile = openFiles()

    print("Assignment #3 - Search Engine")
    userInput = getUserInput()

    while userInput != "q":
        # Start the search time
        startTime = int(time.time() * 1000)
        
        # Get a smaller dictionary from the indexer from the result of the userInput
        indexDict = search(userInput)

        if len(indexDict) == 0:
            print("No results found with all words in a document.")
            endTime = int(time.time() * 1000)
        else:
            # Create a matrix result from the indexDict
            matrix = createMatrix(indexDict)

            # Get the top 5 documents based on the matrix
            documentList = matrixResults(matrix[0], matrix[1])

            endTime = int(time.time() * 1000)

            # Output the documentList
            print("\nResult:\n")
            for i, list in zip(range(1, len(documentList)+1), documentList):
                print(str(i)+ " : "+ list)


        print("\nTotal time to search: " + str(endTime-startTime) + "ms\n")

        userInput = getUserInput()

    closeFile(gFile)
    print("\nClosing the program")
