from tokenizer import *
from indexer import *
from fileRelated import *
import time
import warnings

def createReport(docindCounter):
    ''' return the length of html files, the length of the JSON file (number of unique tokens)
    and the size of our JSON file and
    put it in a txt file or pdf if you know how'''

    # Opens the txtIndex and docIndex files and gets required information to make report
    with open ("txtIndex.txt", "r") as ind:
        numTokens = sum(1 for line in ind)
        fileSize = os.path.getsize("txtIndex.txt")
        fileDoc = open("docIndex.json")
        data = json.load(fileDoc)
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
    
    docIDInd = 0
    allTokens = {}
    resetIndexFiles()
    "iterate through DEV directory and have each file go through the below"
    # Open the initial DEV directory


    # Tracks the total time of the index creation process
    seconds = time.time()
    local_time = time.ctime(seconds)

    warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


    # Loops through the files to be indexed
    for child in Path("DEV").iterdir():
        # discard hidden files
        if not child.name.startswith('.'):
            # Open the subdirectories
            for child2 in Path(child).iterdir():
                if not child2.name.startswith('.'):
                    docIDInd+=1
                    print(docIDInd)
                    # add parsed tokens to allTokens dictionary to keep track of tokens and their weighted frequencies'
                    tokens = openHtml(child2, docIDInd)
                    createIndex(tokens, docIDInd)
                    

    # Final dump of dictionaries in memory to jsons in indexFiles
    dumpGlobalIndexToFiles()

    # Merges the indexFiles into a single txt file
    mergeAndMakeIndDict()

    # Prints start and end time of the index creation
    seconds2 = time.time()
    local_time2 = time.ctime(seconds2)
    print("start time:", local_time)
    print("end time:", local_time2)

    # Creates report of the size of index files
    createReport(docIDInd)