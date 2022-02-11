from importlib.resources import path
from tokenizer import *
from indexer import *
import json
import os

# Shaun
def createReport():
    ''' return the length of html files, the length of the JSON file (number of unique tokens)
    and the size of our JSON file and
    put it in a txt file or pdf if you know how '''

    file = open('index.json')
    data = json.load(file)
    
    numTokens = len(data)
    fileSize = os.path.getsize('index.json')
    numDocs = 0
    for listPairs in data:
        numDocs += len(listPairs[0])
    file.close()

    with open("report.txt", "r") as file:
        file.write(f"Number of unique tokens: {numTokens}")
        file.write(f"Number of documents {numDocs}")
        file.write(f"Size of Index (bytes): {fileSize}")


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


if __name__=="__main__":
    "NOTE: There are 55,393 files so WILL take a while"
    docIDInd = 0
    allTokens = {}
    "iterate through DEV directory and have each file go through the below"
    for subdir, dirs, files in os.walk('DEV'):
        print(str(files))
        tokens = openHtml(files)
        parsedTokens = parseTokens(tokens)
        'add parsed tokens to allTokens dictionary to keep track of tokens and their frequencies'
        createIndex(parsedTokens, docIDInd)
        docIDInd+=1
        for filename in files:
            addPathToDocInd(os.path.join(dirs, filename), docIDInd)
        


