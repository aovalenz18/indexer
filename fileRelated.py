import json
import os
from pathlib import Path

#Ayako
def resetIndexFiles():
    '''
    Deletes all of the indexFile's data
    '''
    for i in range(0,10):
        filePath = "indexFiles/" + str(i) + ".json"
        # open file 
        file = open(filePath, "r+") 
        
        # absolute file positioning
        file.seek(0) 
        
        # to erase all data 
        file.truncate()
        
    for i in range(97, 123): #a-z
        filePath = "indexFiles/" + chr(i) + ".json"
        file = open(filePath, "r+") 
        file.seek(0)
        file.truncate()

#Ayako
def getIndexFilePath(token):
    '''
    token: single token
    returns the file path for which indexfile to look at
    '''
    return "indexFiles/" + token[0] + ".json"
    

