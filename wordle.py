from termcolor import colored
import random
iport requests
import os

CHEATS = False #Set to True to see the correct answer
WORD_LIST_URL = "https://raw.githubusercontent.com/TravellerEntity/wordle/main/clean.txt"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALLOWED_GUESSES = 6
WIN_STATEMENTS = [ #Taken from the original Wordle
    "Genius",
    "Magnificent",
    "Impressive",
    "Splendid",
    "Great",
    "Phew"
]
validWords = requests.get(WORD_LIST_URL).text.split()
targetWord = random.choice(validWords)
userGuess = ""
hints = []
letterHints = []
for i in range(26):
    letterHints.append(0)

def printHints():
    for i in range(len(hints)): #Print previous guesses
        currentHint = hints[i]
        stringToPrint = ""
        for i in range(5):
            color = checkLetter(currentHint[i], targetWord, i)
            if(color == 3):
                highlightColor = "on_green"
            elif(color == 2):
                highlightColor = "on_yellow"
            else:
                highlightColor = "on_dark_grey"
            stringToPrint += colored(currentHint[i],"white",highlightColor)
        print(stringToPrint)
    if(len(hints)<ALLOWED_GUESSES): #Print the grey space at the end
        for i in range(len(hints), ALLOWED_GUESSES):
            stringToPrint = ""
            for i in range(5):
                stringToPrint += colored(" ","white","on_light_grey")
            print(stringToPrint)
    print("")

def checkLetter(letter, target, index):
    if(letter == target[index]):
        return 3
    elif(letter in target):
        return 2
    else:
        return 1

def updateAvailableLetters():
    for i in range(len(hints)):
        word = hints[i]
        for c in range(5):
            letter = word[c]
            col = checkLetter(letter, targetWord, c)
            letterHints[ALPHABET.index(letter)] = col

def printAvailableLetters():
    letters = ""
    for i in range(26):
        letter = letterHints[i]
        if letter == 3:
            highlight = "on_green"
            color = "white"
        elif letter == 2:
            highlight = "on_yellow"
            color = "white"
        elif letter == 1:
            highlight = "on_dark_grey"
            color = "white"
        else:
            highlight = "on_light_grey"
            color = "black"
        letters += colored(ALPHABET[i], color, highlight)
    print(letters)

def printLogo():
    logo = ""
    word = "WORDLE"
    highlights = ["on_green","on_yellow","on_dark_grey","on_green","on_yellow","on_dark_grey"]
    for i in range(len(word)):
        letter = colored(word[i],"white",highlights[i])
        logo += letter
    print(logo + "\n")

def guess():
    while True:
        inputText = colored("["+str(ALLOWED_GUESSES-len(hints))+"]","black","on_light_grey")
        userGuess = input(inputText)
        if(userGuess in validWords and len(userGuess)==5):
            hints.append(userGuess)
            break
        else:
            print(colored("Invalid guess","white","on_red"))
    return userGuess

while True:
    os.system("clear")
    printLogo()
    printHints()
    if(userGuess==targetWord):
        win = True
        break
    elif(len(hints)>ALLOWED_GUESSES-1):
        win = False
        break
    if(CHEATS):
        hintMsg = "The word is: "+targetWord
        print(colored(hintMsg, "light_grey"))
    printAvailableLetters()
    userGuess = guess()
    updateAvailableLetters()

if(win):
    statement = WIN_STATEMENTS[len(hints)-1]
    print(colored(statement, "white", "on_green"))
else:
    print(colored(targetWord.upper(), "white", "on_red"))
    
