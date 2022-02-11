import json
import re
from bs4 import BeautifulSoup

def openHtml(file):
    '''Open files in DEV folder, go through all JSON files and gather text and tokens'''
    'returns a list of all tokens in the html page '
    newFile = open(file)
    fileData = json.load(newFile, "r") #file data is now a dictionary

    soup = BeautifulSoup(fileData["content"], 'html.parser')  # creates the soup object to extract all the text

    fullText = soup.get_text().lower() # gets all text from the document in one string

    #tokenizes strings and separates hyphenated words
    tokenizer = re.findall(r"[a-zA-Z0-9]+", fullText)
    tokens = tokenizer.tokenize(fullText)

    # create list of tokens
    filteredTokens = [word for word in tokens.split()]
    return filteredTokens

def parseTokens(tokens):
    'stemming, tokenizing and frequency, do not take out stopwords'
    'return a list of parsed tokens'
    pass

