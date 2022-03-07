from heapq import merge
import json
import nltk
import io
import os
from pathlib import Path
import math


# Holds on to current indexes
globalIndex = {}

# Stores temporary document ID
globalDocID = {}


def createIndex(tokens: [str], html: int):
    """creates the index of all tokens with list of postings
    JSON file structure:
    token: [ [html,frequency] ]
    keep appending to value list """

    for tokenTuple in tokens:
        token = tokenTuple[0]
        weight = tokenTuple[1]
        if token not in globalIndex:
            globalIndex[token] = [[html, weight]]
        else:
            globalIndex[token].append([html, weight])

    if html % 15000 == 0: 
        dumpGlobalIndexToFiles()


def dumpGlobalIndexToFiles():
    '''
    Dumps the information to the files depending on token's first letter.
    First sort the global index by key alphabetically
    Divide the dictionaries into sections: a-h, i-p, q-z + #
    Update each file according to each section-> file update
    '''
    print("Dumping to files\n")

    dictList = {"a":{}, "b":{}, "c":{}, "d":{}, "e":{}, "f":{}, "g":{}, 
                "h":{}, "i":{}, "j":{}, "k":{}, "l":{}, "m":{}, "n":{}, 
                "o":{}, "p":{}, "q":{}, "r":{}, "s":{}, "t":{}, "u":{}, 
                "v":{}, "w":{}, "x":{}, "y":{}, "z":{}, 
                "0":{}, "1":{}, "2":{}, "3":{}, "4":{}, 
                "5":{}, "6":{}, "7":{}, "8":{}, "9":{}, "'":{}}

    for token in globalIndex:
        #print(token[0])
        dictList[token[0]][token] = globalIndex[token]

    # Refresh the global index
    globalIndex.clear()

    #update file with the sud-dictionaries
    for dictChar in dictList:
        if dictChar == "'":
            updateFile(dictList[dictChar], "z.json")
        else:
            updateFile(dictList[dictChar], str(dictChar)+".json")



    #-----------UPDATE THE DOCINDEX.JSON-----------
    file = open("docIndex.json", "r+")
    
    
    # check if size of file is 0
    # update docIdFileDict depending on if file have prefilled information or not
    if os.stat("docIndex.json").st_size != 0:
        docIdFileDict = json.load(file)
        docIdFileDict.update(globalDocID)
    else:
        docIdFileDict = globalDocID

    # write to file
    file.truncate(0)
    file.seek(0, io.SEEK_END)
    json.dump(docIdFileDict, file, indent=4)

     # close file
    file.close()

    globalDocID.clear()


def updateFile(indexDict: dict, fileName):
    '''
    indexDict - index list taken from the global index
    fileName - name of the file that we are updating
    '''
    # open the file from indexFiles/"fileName"
    filePath = "indexFiles/" + fileName
    file = open(filePath, "r+")
    

    fileDict = {}
    # check if size of file is 0
    # set the fileDict to empty or load in prefilled in dictionary from file
    if os.stat(filePath).st_size != 0:
        fileDict = json.load(file)

    # compare indexDict and loaded dictionay and update the loaded dictionary
    for token in indexDict:
        if token in fileDict:
            # Delete later when not using old indexing
            '''
            # merge posting list from indexDict to fileDict's posting list
            fileDict[token][0].update(indexDict[token][0])
            
            #update the doc frequency by adding 
            fileDict[token][1] += indexDict[token][1]
            '''
            # merge posting list from indexDict to fileDict's posting list
            fileDict[token] = fileDict[token] + indexDict[token]
        else:
            fileDict[token] = indexDict[token]

    # write to file
    #file.seek(0)
    file.truncate(0)
    file.seek(0, io.SEEK_END)
    json.dump(fileDict, file, indent=4)

     # close file
    file.close()


def mergeAndMakeIndDict():
    '''
    Merges each of the index jsons into a single text file and creates a dictionary
    that keeps track of each token and their line number in the
    index file
    '''

    # clear file before running
    with open("txtIndex.txt", "a") as txtFile:
        txtFile.truncate(0)
    # create dictionary with token and line num
    lineNumDict = {}
    
    # load json into dict
    linenum = 0
    for child in Path('indexFiles').iterdir():
        file = open(child)
        data = json.load(file)
        # parse dict lists into "word docFreq docid,weight/tf..."
        with open("txtIndex.txt", "a") as txtFile:
            for token, postList in data.items():
                numDocsWithToken = len(postList)
                tokenStr = f"{token} "
                for post in postList:
                    tfidf = (1 + math.log(post[1])) * (math.log(55393/numDocsWithToken))
                    tokenStr += f"{post[0]},{tfidf} "
                # write to single text file
                txtFile.write(f"{tokenStr} \n")
                linenum += 1
                # add token to lineNumDict
                lineNumDict[token] = linenum
                

    # store dictionary in a json
    with open("lineNums.json", 'r+') as jsonFile:
        jsonFile.truncate(0)
        jsonFile.seek(0, io.SEEK_END)
        json.dump(lineNumDict, jsonFile, indent=4)