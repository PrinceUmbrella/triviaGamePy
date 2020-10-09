class Question:
    def __init__(self, questionJson, category):
        self.questionJson = questionJson
        self.category = category
        self.setQuestion()
        self.setAnswer()
        self.setPoints()
        self.setOptions()
        self.seen = False

    def __str__(self):
        return self.question

    def setOptions(self):
        self.options = self.questionJson.options

    def getOptions(self):
        return self.options

    def setQuestion(self):
        self.question = self.questionJson.question

    def getQuestion(self):
        return self.question

    def getCategory(self):
        return self.category

    def setAnswer(self):
        self.answer = self.questionJson.answer

    def getAnswer(self):
        return self.answer

    def setPoints(self):
        self.points = self.questionJson.worth

    def getPoints(self):
        return self.points

    def isSelected(self):
        return self.seen
