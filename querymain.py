from interface import *
from query import *
import time


'''Main part of query program, have terminal interface to access indexer
Get user input and call outside functions to get the query results'''
if __name__=="__main__":

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

            # For testing search
            #indexDict = search(userInput)
            #print(indexDict)
        
        print("\nTotal time to search: " + str(endTime-startTime) + "ms\n")

        userInput = getUserInput()

    print("\nClosing the program")
