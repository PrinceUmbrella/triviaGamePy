"""
Leoul Tilahun
Jesus Arredondo
DeAnda Little
Royce Payne
Trivia Game
"""

from gameClasses.Question import Question
from gameClasses.Player import Player
from types import SimpleNamespace
from prettytable import PrettyTable
import json
import random

NUMBER_OF_QUESTION_PER_PLAYER = 5
NUMBER_OF_PLAYERS = 2
# Parse JSON into an object with attributes corresponding to dict keys.
questionInput = json.load(open("questionsInput.json"),
                          object_hook=lambda d: SimpleNamespace(**d))

# function initiates the game


def gamePlay():
    questionList = []
    playerList = []
    for category in questionInput.questionsList:
        questionList += unpackQuestion(category)
    random.shuffle(questionList)
    # numberOfPlayers = int(input("Please Enter the number of players: "))
    # player list an array of the player objects

    playerList = getPlayersInfo(NUMBER_OF_PLAYERS)

    print(PrettyTable(["Let's Start The Game"]))
    countt = 0
    totalQuestion = 0

    # The game stops when a total of 10 question have been asked
    while (totalQuestion < NUMBER_OF_PLAYERS * NUMBER_OF_QUESTION_PER_PLAYER):
        currentPlayerName = playerList[totalQuestion %
                                       NUMBER_OF_PLAYERS].getName()
        currentPlayerScore = playerList[totalQuestion %
                                        NUMBER_OF_PLAYERS].getScore()
        question = questionList.pop(0)
        options = question.getOptions()

        print(f"{currentPlayerName} Turn: Current Score {currentPlayerScore}")


` print("\n")
        # question is displayed
        question.printQuestion()
        answer = input("Select your answer: ")

        # When a player chooses their answer it either incorrect or correct
        if (options[int(answer)-1] == question.getAnswer()):
            playerList[totalQuestion %
                       NUMBER_OF_PLAYERS].setScore(question.getPoints())
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

    # When the game ends the score board is displayed
    finalScoreTable = PrettyTable(["Name", "Score"])
    for i in playerList:
        finalScoreTable.add_row([i.getName(), i.getScore()])

    print("\n")
    print(finalScoreTable)
    print(f"The winner(s) : {', '.join(getWinner(playerList))}")

# function that gets the name and sets them to an array of players


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

# function that gets the list of questions from the JSON file


def unpackQuestion(categoryPack):
    questionList = []
    for ques in categoryPack.questions:
        questionList.append(Question(ques, categoryPack.category))
    return questionList
# function that determines who's the winner


def getWinner(playerList):
    maxScore = 0
    winner = []
    for player in playerList:
        if (player.getScore() > maxScore):
            maxScore = player.getScore()
            winner = [player.getName()]
        elif (player.getScore() == maxScore):
            winner.append(player.getName())
    return winner


gamePlay()
