import json
import nltk
import io
import os

# Holds on to current indexs
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
        
        globalIndexCounter += 1        # will add this part when updating file part is done
        #print(token)

    
    # change to update to file when globalIndexCounter > 300000 ?
    if globalIndexCounter > 300000:
        dumpGlobalIndexToFiles()

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
    subDict1 = {}
    subDict2 = {}
    subDict3 = {}

    for token in globalIndex:
        if token[0] >= "a" and token[0] <= "h":
            subDict1[token] = globalIndex[token]
        elif token[0] >= "i" and token[0] <= "p":
            subDict2[token] = globalIndex[token]
        else:
            subDict3[token] = globalIndex[token]

    # Refresh the global index and counter
    globalIndex.clear()
    globalIndexCounter = 0

    #update file with the sud-dictionaries
    updateFile(subDict1, "indexFile1.json")
    updateFile(subDict2, "indexFile2.json")
    updateFile(subDict3, "indexFile3.json")


def updateFile(indexDict, fileName):
    '''
    indexDict - index list taken from the global index
    fileName - name of the file that we are updating
    '''
    # open the file from indexFiles/"fileName"
    filePath = "indexFiles\\" + fileName
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
        jsonFile.seek(0)
        jsonFile.truncate()
        json.dump(fileDict, jsonFile, indent=4)

