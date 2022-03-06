HOW TO START CREATING THE INDEXER

Please run the file main.py to start creating the indexer.

Once you start running the file, it will start outputing a series of numbers starting from 1.

These numbers represent the document ID numbers from 1 to the total of 55393 files.
 
The indexer will be dumped to the files in the indexFiles folder every 15000 json files 
it has parsed. 

In total there will be 4 dumps and in the end, the indexer will be compiled into one file called
txtIndex.txt.

This will contain all of the terms with their respective posting list that contains the document ID and 
the tf-idf score for that term and document.




HOW TO RUN THE SEARCH

Please run the file querymain.py to start the search.

There may be a small delay from running until you are able to search while the information from the 
database is being loaded into memory.

Once it has finished loading, you will be prompted to enter in a query.

The search query will accept ONLY alphanumeric letters and apostrophes.

If it detects any other characters or error, the user will be prompted to re-enter another query.

Once an acceptable query is entered, the search will take place and output the top 10 results and 
total time it took to search.

The program will then ask you to enter another query.

To stop the program enter in "q" to the query.
