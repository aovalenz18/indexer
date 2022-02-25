from heapq import merge
import json
import nltk
import io
import os
from pathlib import Path

# Holds on to current indexs
import indexer

globalIndex = {}

# Counter for how many words are in globalIndex
globalIndexCounter = 0

def createIndex(tokens: [str], html: int):
    """creates the index of all tokens with list of postings
    JSON file structure:
    token: [ [html,frequency] ]
    keep appending to value list """

    if html == 1:
        # Delete the content of index.json
        file = open("index.json", "r+") 
        file.seek(0) 
        file.truncate() 


    # create a frequency dictionary for all the tokens
    freqDict = nltk.FreqDist(tokens)
    # print(tokens)

    #gCount = indexer.globalIndexCounter

    # go through all tokens and add to the global indexer
    for token in freqDict:
        
        '''
        # Anthony's work
        postings = [{html: [freqDict[token]]}, 0]
        if token in globalIndex:
            # list of postings
            postings = globalIndex[token]
            # add key into document dictionary
            frequency = postings[0][html][0]
            updatedFrequency = frequency + freqDict[token]
            postings[0][html][0] = updatedFrequency # this will have an updated list
        '''

        if token in globalIndex:
            # add in the new posting
            globalIndex[token][0][html] = [freqDict[token]] #freqDict[token] - counter
            
            #update the doc frequency
            globalIndex[token][1] += 1
        else:
            globalIndex[token] = [{html: [freqDict[token]]}, 1]

            #gCount += 1
            # will add this part when updating file part is done

            #globalIndexCounter += 1        # will add this part when updating file part is done

        #print(token)

    
    # change to update to file when globalIndexCounter > 300000 ?
    if html % 10000 == 0:       #gCount > 300000:
        dumpGlobalIndexToFiles()
        #gCount = indexer.globalIndexCounter

    #indexer.globalIndexCounter = gCount

    '''
    # PUT WRITING INTO INDEX.JSON IN THE MAIN FOR NOW SO IT WILL ONLY CALL ONCE - AYAKO
    # if index is a multiple of 100, we dump into jsonFile and clear the global index
    #if html % 100 == 0 or html < 100:
    with open('index.json', 'r+') as jsonFile:
        jsonFile.seek(0, io.SEEK_END)
        json.dump(globalIndex, jsonFile, indent=4)

        #globalIndex.clear()
    '''


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
                "5":{}, "6":{}, "7":{}, "8":{}, "9":{}}

    for token in globalIndex:
        #print(token[0])
        #tempDict = dictList[token[0]]
        #tempDict[token] = globalIndex[token]
        #dictList[token[0]] = tempDict
        dictList[token[0]][token] = globalIndex[token]

    # Refresh the global index and counter
    globalIndex.clear()
    #indexer.globalIndexCounter = 0

    #update file with the sud-dictionaries
    for dictChar in dictList:
        updateFile(dictList[dictChar], str(dictChar)+".json")


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
                # merge posting list from indexDict to fileDict's posting list
                fileDict[token][0].update(indexDict[token][0])
                
                #update the doc frequency by adding 
                fileDict[token][1] += indexDict[token][1]
        else:
            fileDict[token] = indexDict[token]

     # close file
    file.close()

    # fill file with loaded dictionary (fileDict)- 
    # maybe need to delete content beforehand?
    # maybe sort the dictionary if wanted to
    with open(filePath, 'r+') as jsonFile:
        jsonFile.truncate(0)
        jsonFile.seek(0, io.SEEK_END)
        json.dump(fileDict, jsonFile, indent=4)


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
                tokenStr = f"{token} {len(postList)} "
                for post in postList:
                    tokenStr += f"{post[0]},{post[1]} "
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

if __name__ == "__main__":
    mergeAndMakeIndDict()