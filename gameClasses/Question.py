from prettytable import PrettyTable
import random

"""
Question object has the question and array of possible answers.
Holds the category, answer, and worth of each question
"""


class Question:
    def __init__(self, questionJson, category):
        self.questionJson = questionJson
        self.category = category
        self.setQuestion()
        self.setAnswer()
        self.setPoints()
        self.setOptions()
        self.seen = False
    # function that lets us print the question

    def __str__(self):
        return self.question
    # function that sets option

    def setOptions(self):
        random.shuffle(self.questionJson.options)
        self.options = self.questionJson.options
    # function that allows us to get the possible answers

    def getOptions(self):
        return self.options
    # function that sets the question

    def setQuestion(self):
        self.question = self.questionJson.question
    # function that lets us get the question

    def getQuestion(self):
        return self.question
    # function that set category

    def getCategory(self):
        return self.category
    # function that sets the answer

    def setAnswer(self):
        self.answer = self.questionJson.answer
    # function that gets the answer

    def getAnswer(self):
        return self.answer
    # function that sets points

    def setPoints(self):
        self.points = self.questionJson.worth
    # function that gets points

    def getPoints(self):
        return self.points
    # function that lets us know if the card has been seen before

    def isSelected(self):
        return self.seen
    # using the PrettyTable import nicely displays the question object
    # With a question title and the options

    def printQuestion(self):
        questionCard = PrettyTable([self.question])

        counter = 0
        for opt in self.options:
            questionCard.add_row([f"{counter + 1}: {opt}"])
            counter += 1
        scoreCard = PrettyTable([f"For {self.points} points: "])
        print(questionCard)
        print(scoreCard)
