"""
Player object holds each player's information
such as name and score 
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.formatNames()

    def getName(self):
        return self.name

    def setScore(self, increase):
        self.score = self.score + increase

    def getScore(self):
        return self.score

    def formatNames(self):
        self.name = self.name.lower()
        firstAndLastNames = self.name.split(" ")
        self.name = " ".join([i[0].upper() + i[1:]
                              for i in firstAndLastNames if i != ''])
