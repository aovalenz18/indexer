from interface import *
from query import *
import json

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
        # Add this part when the functions gets done

        # Get a smaller dictionary from the indexer from the result of the userInput
        indexDict = search(userInput)

        # Create a matrix result from the indexDict
        matrix = createMatrix(indexDict)

        # Get the top 5 documents based on the matrix
        documentList = matrixResults(matrix[0], matrix[1])

        # Output the documentList
        # printResult(documentList)
        print(documentList)

        # Used to see what the parsed userInput look like
        print(userInput)

        # For testing search
        # indexDict = search(userInput)
        # print(indexDict)

        userInput = getUserInput()

    closeFile(gFile)
    print("\nClosing the program")


    pass
