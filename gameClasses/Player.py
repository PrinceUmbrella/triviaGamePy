class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def getName(self):
        return self.name

    def setScore(self, increase):
        self.score = self.score + increase

    def getScore(self):
        return self.score
