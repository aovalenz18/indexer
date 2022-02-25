import nltk
from nltk.stem import PorterStemmer
import json
import re
from bs4 import BeautifulSoup
from selectolax.parser import HTMLParser
import lxml
import cchardet
import os
from urllib.request import urlopen

from indexer import globalDocID

# kazeem
def openHtml(file, docID):
    '''Open files in DEV folder, go through all JSON files and gather text and tokens'''
    'returns a list of all tokens in the html page '
    # return a list of tuples (word, weight) and the weight is going to include the frequency,
    # type of word, and at the end call parse tokens on all the words

    newFile = open(file)
    fileData = json.load(newFile) #file data is now a dictionary
    newFile.close()

    soup = BeautifulSoup(fileData["content"], "lxml")  # creates the soup object to extract all the text
    fullText = soup.get_text().lower() # gets all text from the document in one string

    try:
        soup2 = BeautifulSoup(urlopen(fileData["url"]), "lxml")  # creates the soup object to extract url
        url = soup2.get_text() # gets all text from the document in one string
        url = url.split('#')
        url = url[0]
    except:
        url = "ERROR"

    #get standard tokens in a list
    tokens = parseTokens(re.findall(r"[a-zA-Z0-9]+", fullText))


    #create a weight dictionary with the frequency as the starting weight
    freqDict = nltk.FreqDist(tokens)

    #TODO: account for broken html & adjust weight system also make sure parser is working correctly
    #titles
    for tags in soup.find_all("title"):
        tokens = parseTokens(re.findall(r"[a-zA-Z0-9]+", tags.text))
        for token in tokens:
            freqDict[token] += 20

    #headers
    heading_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
    for tags in soup.find_all(heading_tags):
        tokens = parseTokens(re.findall(r"[a-zA-Z0-9]+", tags.text))

        if tags.name == "h1":
            for token in tokens:
                freqDict[token] += 20
        elif tags.name == "h2":
            for token in tokens:
                freqDict[token] += 15
        elif tags.name == "h3":
            for token in tokens:
                freqDict[token] += 10
        elif tags.name == "h4":
            for token in tokens:
                freqDict[token] += 8
        elif tags.name == "h5":
            for token in tokens:
                freqDict[token] += 6
        elif tags.name == "h6":
            for token in tokens:
                freqDict[token] += 5

    #bolds
    for tags in soup.find_all("b"):
        tokens = parseTokens(re.findall(r"[a-zA-Z0-9]+", tags.text))
        for token in tokens:
            freqDict[token] += 5

    #strongs
    for tags in soup.find_all("strong"):
        tokens = parseTokens(re.findall(r"[a-zA-Z0-9]+", tags.text))
        for token in tokens:
            freqDict[token] += 5

    # update global dictionary with the doc ID key
    globalDocID[docID] = {'path': str(file), 
                          'url': url}


    tokens = [(key,weight) for key,weight in freqDict.items()]
    return tokens



def parseTokens(tokens):
    """porter stemming, do not take out stopwords"""
    'return a list of parsed tokens'
    'Ayako'
    ps = PorterStemmer()
    for index, word in enumerate(tokens):
        tokens[index] = ps.stem(word)
    return tokens

