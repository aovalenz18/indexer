HOW TO START CREATING THE INDEXER

Please run the file main.py to start creating the indexer.

Once you start running the file, it will start outputing a series of numbers starting from 1.

These numbers represent the document ID numbers and you can tell how many out of the total
55393 json files you have gone through.
 
The indexer will be dumped to the files in the indexFiles folder every 15000 json files 
it has gone through. 

In total there will be 4 dumps and in the end, the indexer will be compiled to one file called
txtIndex.txt.

This will contain all of the terms will their posting list that contains the document ID and 
the tf-idf score for that term and document.




HOW TO RUN THE SEARCH

Please run the file querymain.py to start the search.

In the beginning it may take some time before you can search a query since the information from 
the database is being loading in first.

Once it has finished loading, it will then ask you to enter in a query.

The search query will accept ONLY alphanumeric letters and apostrophes.

If it detects any other characters or error, the user will be prompted to reenter another query.

Once an acceptable query is entered, the search will take place and outputs the top 10 results and 
total time it took to search to the interface.

The program will then ask you to enter another query.

To stop the program enter in "q" to the query.
