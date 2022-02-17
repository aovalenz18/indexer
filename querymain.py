from interface import *
from query import *


'''Main part of query program, have terminal interface to access indexer
Get user input and call outside functions to get the query results'''
if __name__=="__main__":

    print("Assignment #3 - Search Engine")
    userInput = getUserInput()

    while userInput != "q":
        # Add this part when the functions gets done
        """
        # Get a smaller dictionary from the indexer from the result of the userInput
        indexDict = search(userInput)

        # Create a matrix result from the indexDict
        matrix = createMatrix(indexDict)

        # Get the top 5 documents based on the matrix
        documentList = matrixResults(matrix, indexDict)

        # Output the documentList
        # printResult(documentList)
        print(documentList)
        """
        
        

        # Used to see what the parsed userInput look like
        print(userInput)

        # For testing search
        #indexDict = search(userInput)
        #print(indexDict)

        userInput = getUserInput()

    print("\nClosing the program")

    pass