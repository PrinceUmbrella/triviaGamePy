from gameClasses.Question import Question
from gameClasses.Player import Player
from types import SimpleNamespace
import json
import random

# Parse JSON into an object with attributes corresponding to dict keys.
questionInput = json.load(open("questionsInput.json"),
                          object_hook=lambda d: SimpleNamespace(**d))


def gamePlay():
    questionList = []
    playerList = []
    for elements in questionInput.questionsList:
        questionList += unpackQuestion(elements)
    random.shuffle(questionList)
    numberOfPlayers = int(input("Please Enter the number of players: "))

    playerNames = []
    for i in range(numberOfPlayers):
        name = input(f"Please Enter the name for Player {i + 1}: ")
        while (name in playerNames):
            name = input(
                f"Name already exsits, Please Enter the name for Player {i + 1}: ")
        playerList.append(Player(name, i))
        playerNames.append(name)
        print("\n")


def unpackQuestion(categoryPack):
    questionList = []
    for ques in categoryPack.questions:
        questionList.append(Question(ques, categoryPack.category))
    return questionList


gamePlay()
