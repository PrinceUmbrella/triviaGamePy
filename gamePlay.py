from gameClasses.Question import Question
from UI.Display import Game
from types import SimpleNamespace
import json
data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.
questionInput = json.load(open("questionsInput.json"),
                          object_hook=lambda d: SimpleNamespace(**d))


questionObj = Question(
    questionInput.questionsList[0].questions[0], questionInput.questionsList[0].category)
print(questionObj)

# Display Question
result = Game(questionObj.getQuestion(), questionObj.getOptions())

print("User's response was: {}".format(repr(result)))

questionObj = Question(
    questionInput.questionsList[0].questions[1], questionInput.questionsList[0].category)
print(questionObj)

# Display Question
result = Game(questionObj.getQuestion(), questionObj.getOptions())

print("User's response was: {}".format(repr(result)))
