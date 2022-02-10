from tokenizer import *
from indexer import *

def createReport():
    ''' return the length of html files, the length of the JSON file (number of unique tokens)
    and the size of our JSON file and
    put it in a txt file or pdf if you know how '''
    pass



if __name__=="__main__":


    allTokens = {}
    "iterate through DEV directory and have each file go through the below"

    file = None
    tokens = openHtml(file)
    parsedTokens = parseTokens(tokens)

    'add parsed tokens to allTokens dictionary to keep track of tokens and their frequencies'
    createIndex(parsedTokens, file)




