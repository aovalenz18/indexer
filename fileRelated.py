import json
import os
from pathlib import Path

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

#Ayako
def getIndexFilePath(token):
    '''
    token: single token
    returns the file path for which indexfile to look at
    '''
    if token[0] >= "a" and token[0] <= "c":
        return "indexFiles/indexFile1.json"
    elif token[0] >= "d" and token[0] <= "f":
        return "indexFiles/indexFile2.json"
    elif token[0] >= "g" and token[0] <= "i":
        return "indexFiles/indexFile3.json"
    elif token[0] >= "j" and token[0] <= "l":
        return "indexFiles/indexFile4.json"
    elif token[0] >= "m" and token[0] <= "n":
        return "indexFiles/indexFile5.json"
    elif token[0] >= "o" and token[0] <= "p":
        return "indexFiles/indexFile6.json"
    elif token[0] >= "q" and token[0] <= "r":
        return "indexFiles/indexFile7.json"
    elif token[0] >= "s" and token[0] <= "t":
        return "indexFiles/indexFile8.json"
    elif token[0] >= "u" and token[0] <= "w":
        return "indexFiles/indexFile9.json"
    else:
        return "indexFiles/indexFile10.json"

