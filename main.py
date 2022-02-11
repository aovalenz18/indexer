from importlib.resources import path
from tokenizer import *
from indexer import *
from pathlib import Path
import json
import os

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



if __name__=="__main__":

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


