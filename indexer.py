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

    gCount = indexer.globalIndexCounter

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

            gCount += 1
            # will add this part when updating file part is done

            # globalIndexCounter += 1        # will add this part when updating file part is done

        #print(token)

    
    # change to update to file when globalIndexCounter > 300000 ?
    if gCount > 300000:
        dumpGlobalIndexToFiles()
        gCount = indexer.globalIndexCounter

    indexer.globalIndexCounter = gCount

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
    subDict1 = {} #a,b,c
    subDict2 = {} #d,e,f
    subDict3 = {} #g,h,i
    subDict4 = {} #j,k,l
    subDict5 = {} #m,n
    subDict6 = {} #o,p
    subDict7 = {} #q,r
    subDict8 = {} #s,t
    subDict9 = {} #u,v,w
    subDict10 = {} #x,y, z, all others

    for token in globalIndex:
        #print(token[0])
        if token[0] >= "a" and token[0] <= "c":
            subDict1[token] = globalIndex[token]
            #print("sub1")
        elif token[0] >= "d" and token[0] <= "f":
            subDict2[token] = globalIndex[token]
            #print("sub2")
        elif token[0] >= "g" and token[0] <= "i":
            subDict3[token] = globalIndex[token]
            #print("sub3")
        elif token[0] >= "j" and token[0] <= "l":
            subDict4[token] = globalIndex[token]
            #print("sub4")
        elif token[0] >= "m" and token[0] <= "n":
            subDict5[token] = globalIndex[token]
            #print("sub5")
        elif token[0] >= "o" and token[0] <= "p":
            subDict6[token] = globalIndex[token]
            #print("sub6")
        elif token[0] >= "q" and token[0] <= "r":
            subDict7[token] = globalIndex[token]
            #print("sub7")
        elif token[0] >= "s" and token[0] <= "t":
            subDict8[token] = globalIndex[token]
            #print("sub8")
        elif token[0] >= "u" and token[0] <= "w":
            subDict9[token] = globalIndex[token]
            #print("sub9")
        else:
            subDict10[token] = globalIndex[token]
            #print("sub10")


    #print("sub1", subDict1)
    #print("sub2", subDict2)
    #print("sub3", subDict3)
    #print("sub4", subDict4)

    # Refresh the global index and counter
    globalIndex.clear()
    indexer.globalIndexCounter = 0

    #update file with the sud-dictionaries
    updateFile(subDict1, "indexFile1.json")
    updateFile(subDict2, "indexFile2.json")
    updateFile(subDict3, "indexFile3.json")
    updateFile(subDict4, "indexFile4.json")
    updateFile(subDict5, "indexFile5.json")
    updateFile(subDict6, "indexFile6.json")
    updateFile(subDict7, "indexFile7.json")
    updateFile(subDict8, "indexFile8.json")
    updateFile(subDict9, "indexFile9.json")
    updateFile(subDict10, "indexFile10.json")


def updateFile(indexDict, fileName):
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