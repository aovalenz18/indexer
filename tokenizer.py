from nltk.stem import PorterStemmer


def openHtml(file):
    '''Open files in DEV folder, go through all JSON files and gather text and tokens'''
    'returns a list of all tokens in the html page '
    pass


def parseTokens(tokens):
    'porter stemming, do not take out stopwords'
    'return a list of parsed tokens'
    'Ayako'
    ps = PorterStemmer()
    for index, word in enumerate(tokens):
        tokens[index] = ps.stem(word)

