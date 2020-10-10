from gameClasses.Question import Question
from gameClasses.Player import Player
from types import SimpleNamespace
from prettytable import PrettyTable
import json
import random


# Parse JSON into an object with attributes corresponding to dict keys.
questionInput = json.load(open("questionsInput.json"),
                          object_hook=lambda d: SimpleNamespace(**d))


def gamePlay():
    questionList = []
    playerList = []
    for category in questionInput.questionsList:
        questionList += unpackQuestion(category)
    random.shuffle(questionList)
    # numberOfPlayers = int(input("Please Enter the number of players: "))
    numberOfPlayers = 2

    playerList = getPlayersInfo(numberOfPlayers)

    print(PrettyTable(["Let's Start The Game"]))
    countt = 0
    totalQuestion = 0

    while (totalQuestion < 10):
        currentPlayerName = playerList[totalQuestion %
                                       numberOfPlayers].getName()
        currentPlayerScore = playerList[totalQuestion %
                                        numberOfPlayers].getScore()
        question = questionList.pop(0)
        options = question.getOptions()
        print(f"{currentPlayerName} Turn: Current Score {currentPlayerScore}")

        question.printQuestion()
        answer = input("Select your answer: ")

        if (options[int(answer)-1] == question.getAnswer()):
            playerList[totalQuestion %
                       numberOfPlayers].setScore(question.getPoints())
            print(PrettyTable(
                [f"Correct Answer! Your current score is {currentPlayerScore + question.getPoints()}"]))
        else:
            incorrectTable = PrettyTable(
                [f"Incorrect Answer! The answer is {question.getAnswer()}"])
            incorrectTable.add_row(
                [f"Your current score is still {currentPlayerScore}"])
            print(incorrectTable)
        print("\n")
        totalQuestion += 1
    finalScoreTable = PrettyTable(["Name", "Score"])
    for i in playerList:
        finalScoreTable.add_row([i.getName(), i.getScore()])
    print("\n")
    print(finalScoreTable)


def getPlayersInfo(numberOfPlayers):
    playerNames = []
    playerList = []
    for i in range(numberOfPlayers):
        name = input(f"Please Enter the name for Player {i + 1}: ")
        while (name in playerNames):
            name = input(
                f"Name already exsits, Please Enter the name for Player {i + 1}: ")
        playerList.append(Player(name))
        playerNames.append(name)
    return playerList


def unpackQuestion(categoryPack):
    questionList = []
    for ques in categoryPack.questions:
        questionList.append(Question(ques, categoryPack.category))
    return questionList


gamePlay()
