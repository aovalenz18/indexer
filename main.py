from tokenizer import *
from indexer import *
from fileRelated import *
import time
import warnings

def createReport(docindCounter):
    ''' return the length of html files, the length of the JSON file (number of unique tokens)
    and the size of our JSON file and
    put it in a txt file or pdf if you know how

    numTokens = 0
    fileSize = 0
    numDocs = docindCounter

    for i in range(0,10):
        filePath = "indexFiles/" + str(i) + ".json"
    
        file = open(filePath)

        data = json.load(file)
        numTokens += len(data)
        fileSize += os.path.getsize(filePath)

        file.close()
    
    for i in range(97, 123): #a-z
        filePath = "indexFiles/" + chr(i) + ".json"
        file = open(filePath)

        data = json.load(file)
        numTokens += len(data)
        fileSize += os.path.getsize(filePath)

        file.close()'''

    with open ("txtIndex.txt", "r") as ind:
        numTokens = sum(1 for line in ind)
        fileSize = os.path.getsize("txtIndex.txt")
        data = json.load("docIndex.json")
        numDocs = len(data)

        with open("report.txt", "r+") as file:
            file.truncate(0)
            file.write("Assignment 3 Milestone 1 Report \n")
            file.write(f"Number of unique tokens: {numTokens}\n")
            file.write(f"Number of documents {numDocs}\n")
            file.write(f"Size of Index (bytes): {fileSize}\n")



# Ayako
# Used for testing - may delete later if unnecessary
# prints out the path and htmlSite for specified docIndex
def printIndex(index):
	index = str(index)
	f = open ("docIndex.json", "r")
	
	# Reading from file
	data = json.load(f)
	
	print(data[index]["path"])
	print(data[index]["url"])
	
	f.close()


if __name__== "__main__":
    "NOTE: There are 55,393 files so WILL take a while"
    docIDInd = 0
    allTokens = {}
    resetIndexFiles()
    "iterate through DEV directory and have each file go through the below"
    #Open the initial DEV directory
    
    seconds = time.time()
    local_time = time.ctime(seconds)

    warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

    for child in Path("DEV").iterdir():
        #discard hidden files
        if not child.name.startswith('.'):
            #Open the subdirectories
            for child2 in Path(child).iterdir():
                if not child2.name.startswith('.'):
                    docIDInd+=1
                    print(docIDInd)
                    tokens = openHtml(child2, docIDInd)
                    #add parsed tokens to allTokens dictionary to keep track of tokens and their frequencies'
                    createIndex(tokens, docIDInd)
                    

    dumpGlobalIndexToFiles()
    mergeAndMakeIndDict()

    seconds2 = time.time()
    local_time2 = time.ctime(seconds2)
    print("start time:", local_time)
    print("end time:", local_time2)
    
    '''
    with open('index.json', 'r+') as jsonFile:
        jsonFile.seek(0, io.SEEK_END)
        json.dump(globalIndex, jsonFile, indent=4)
    '''
    
    createReport(docIDInd)
        


