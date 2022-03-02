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

    validationPass = False

    while validationPass == False:
        userInput = input("Enter your search query (To quit, enter \"q\"): ").lower()

        if userInput == "q":
            return userInput

        userInput = validate(userInput)

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
    numOfWords1 = len(query.split())

    #tokenizes strings
    inputTokens = re.findall(r"(?:^|(?<= ))[a-zA-Z0-9']+(?= |$)", query)

    if(numOfWords1 != len(inputTokens)):
        print("\nError in the input, please enter in input correctly.\n")
        return []
    
    return parseTokens(inputTokens)
