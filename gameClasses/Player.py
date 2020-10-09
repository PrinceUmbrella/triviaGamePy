class Player:
    def __init__(self, name, playerId):
        self.name = name
        self.score = 0
        self.id = playerId

    def getPlayer(self):
        return self.name

    def setScore(self, increase):
        self.score = self.score + increase

    def getScore(self):
        return self.score

    def getId(self):
        return self.id
