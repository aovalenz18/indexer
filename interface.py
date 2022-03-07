# Ayako

from tokenizer import *

def getUserInput():
    """Output text for user interface, to be called in query main
        - Instructions on how to format response
            Instructions:
            1) words separated by space 
            2) all will be taken in consideration for AND operation
            3) Do not include any punctuation
        
        Returns: valid and parsed tokens of the user input"""

    print("\nNotes/Rules:\n" + 
          "1) Words need to be separated by space\n" +
          "2) The search will be taken in consider for AND operation\n" + 
          "3) Do not include any punctuation beside the aposterphe\n")

    # Used as a indicator on whether the user input a valid input or not
    validationPass = False

    # This will the main part of the user input, will not break till user puts in a
    # valid input
    while validationPass == False:
        userInput = input("Enter your search query (To quit, enter \"q\"): ").lower()

        # Returns q so the outer function can successfully close the program
        if userInput == "q":
            return userInput

        # Checks if the input is valid and get a list either none or stemmed 
        # version of the user input.
        userInput = validate(userInput)

        # If the length was 0, then it means the user input was not valid
        if len(userInput) > 0:
            validationPass = True

    return userInput


def validate(query: str):
    """
    :param query: string query from user input
    :return: list of parsed tokens if validated, empty list if not valid

    Function will validate if it is a proper query by tokenizing and parsing the string,
    if one of the tokens are not valid then we will recall
    """

    # Gets the number of words before tokenizing
    numOfWords1 = len(query.split())

    # Tokenizes the input
    # Only finds words that are alphanumeric and/or has aposterphe(s)
    inputTokens = re.findall(r"(?:^|(?<= ))[a-zA-Z0-9']+(?= |$)", query)

    # Checks if the numbers of words are the same before and after tokenization.
    # If false, it means that the user inputed at least one invalid character
    # and the result of the user input will be returned blank
    if(numOfWords1 != len(inputTokens)):
        print("\nError in the input, please enter in input correctly.\n")
        return []
    
    # Returns the stemmed version of the user input if valid
    return parseTokens(inputTokens)
