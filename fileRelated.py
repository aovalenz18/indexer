# Ayako
def resetIndexFiles():
    '''
    Deletes all of the indexFile and doxIndex's data
    '''
    for i in range(0,10):
        filePath = "indexFiles/" + str(i) + ".json"
        # open file 
        file = open(filePath, "r+") 
        
        # absolute file positioning
        file.seek(0) 
        
        # to erase all data 
        file.truncate()

        file.close()
        
    for i in range(97, 123): # a-z
        filePath = "indexFiles/" + chr(i) + ".json"
        file = open(filePath, "r+") 
        file.truncate(0)
        file.close()

    # Delete information in docIndex.json
    file = open("docIndex.json", "r+") 
    file.truncate(0)
    file.close()

# Ayako
def getIndexFilePath(token):
    '''
    token: single token
    returns the file path for which indexfile to look at
    '''
    return "indexFiles/" + token[0] + ".json"
    

