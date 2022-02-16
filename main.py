from tokenizer import *
from indexer import *
import json
import os
from pathlib import Path



def createReport(docindCounter):
    ''' return the length of html files, the length of the JSON file (number of unique tokens)
    and the size of our JSON file and
    put it in a txt file or pdf if you know how '''

    numTokens = 0
    fileSize = 0
    numDocs = docindCounter

    for i in range(1,11):
        filePath = "indexFiles/indexFile" + str(i) + ".json"
    
        file = open(filePath)

        data = json.load(file)
        numTokens += len(data)
        fileSize += os.path.getsize(filePath)

        file.close()

    with open("report.txt", "r+") as file:
        file.truncate(0)
        file.write("Assignment 3 Milestone 1 Report \n")
        file.write(f"Number of unique tokens: {numTokens}\n")
        file.write(f"Number of documents {numDocs}\n")
        file.write(f"Size of Index (bytes): {fileSize}\n")


# Ayako
def addPathToDocInd(path, docIDInd):
    ''' 
    path - path for one file
    docIDInd - document index number
    This function will take a path of a file and 
    append the path to the docIndex.json
    Returns nothing
    '''
    docData = {docIDInd:{'path': path, 
						 'htmlSite': 'testing'}}
	
    if(docIDInd == 1):
        with open("docIndex.json", "r+") as file:
            file.truncate(0) #clears data within file
            file.write(json.dumps(docData, indent=4))
    else:
        with open("docIndex.json", "r+") as file:
            fileData = json.load(file)
            fileData.update(docData)
            file.seek(0)
            json.dump(fileData, file, indent=4)


# Ayako
# Used for testing - may delete later if unnecessary
# prints out the path and htmlSite for specified docIndex
def printIndex(index):
	index = str(index)
	f = open ("docIndex.json", "r")
	
	# Reading from file
	data = json.load(f)
	
	print(data[index]["path"])
	print(data[index]["htmlSite"])
	
	f.close()

#Ayako
def resetIndexFiles():
    '''
    Deletes all of the indexFile's data
    '''
    for i in range(1,11):
        filePath = "indexFiles/indexFile" + str(i) + ".json"
        # open file 
        file = open(filePath, "r+") 
        
        # absolute file positioning
        file.seek(0) 
        
        # to erase all data 
        file.truncate() 


if __name__=="__main__":
    "NOTE: There are 55,393 files so WILL take a while"
    docIDInd = 0
    allTokens = {}
    resetIndexFiles()
    "iterate through DEV directory and have each file go through the below"
    #Open the initial DEV directory
    for child in Path('DEVtesting').iterdir():
        #discard hidden files
        if not child.name.startswith('.'):
            #Open the subdirectories
            for child2 in Path(child).iterdir():
                if not child2.name.startswith('.'):
                    tokens = openHtml(child2)
                    parsedTokens = parseTokens(tokens)
                    #add parsed tokens to allTokens dictionary to keep track of tokens and their frequencies'
                    docIDInd+=1
                    print(docIDInd)
                    createIndex(parsedTokens, docIDInd)
                    addPathToDocInd(str(child2.resolve()), docIDInd)


    dumpGlobalIndexToFiles()
    
    '''
    with open('index.json', 'r+') as jsonFile:
        jsonFile.seek(0, io.SEEK_END)
        json.dump(globalIndex, jsonFile, indent=4)
'''
    
    createReport(docIDInd)
        


