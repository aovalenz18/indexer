from nltk.stem import PorterStemmer
import json
import re
from bs4 import BeautifulSoup

# kazeem
def openHtml(file):
    '''Open files in DEV folder, go through all JSON files and gather text and tokens'''
    'returns a list of all tokens in the html page '
    newFile = open(file)
    fileData = json.load(newFile) #file data is now a dictionary

    soup = BeautifulSoup(fileData["content"], 'html.parser')  # creates the soup object to extract all the text

    fullText = soup.get_text().lower() # gets all text from the document in one string

    #tokenizes strings
    tokens = re.findall(r"[a-zA-Z0-9]+", fullText)

    # create list of tokens
    #filteredTokens = [word for word in tokenizer.split()]
    return tokens


def parseTokens(tokens):
    'porter stemming, do not take out stopwords'
    'return a list of parsed tokens'
    'Ayako'
    ps = PorterStemmer()
    for index, word in enumerate(tokens):
        tokens[index] = ps.stem(word)
    return tokens

