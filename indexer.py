import json
import nltk
import io

# Holds on to current indexs
globalIndex = {}

# Counter for how many words are in globalIndex
globalIndexCounter=0

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
            # globalIndexCounter += 1        # will add this part when updating file part is done
        #print(token)

    '''
    # change to update to file when globalIndexCounter > 30000 ?
    if globalIndexCounter > 30000
        dumpGlobalIndexToFiles()


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


    # Refresh the global index and counter
    globalIndex.clear()
    globalIndexCounter = 0

    pass

def updateFile(indexDict, fileName):
    '''
    indexDict - index list taken from the global index
    fileName - name of the file that we are updating
    '''
    # open the file from indexFiles/"fileName" as r+


    # load dictionary from the file
    fileDict = load function


    # DONE i think...
    # compare indexDict and loaded dictionay and update the loaded dictionary
    for token in indexDict:
        if token in fileDict:
                # merge posting list from indexDict to fileDict's posting list
                fileDict[token][0].update(indexDict[token][0])
                
                #update the doc frequency by adding 
                fileDict[token][1] += indexDict[token][1]
        else:
            globalIndex[token] = indexDict[token]

    
    # fill file with loaded dictionary (fileDict)- 
    # maybe need to delete content beforehand?
    # maybe sort the dictionary if wanted to


    # close file


    pass
