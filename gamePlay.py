from gameClasses.Question import Question
from types import SimpleNamespace
import json
data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.
questionInput = json.load(open("questionsInput.json"),
                          object_hook=lambda d: SimpleNamespace(**d))


questionObj = Question(
    questionInput.questionsList[0].questions[0], questionInput.questionsList[0].category)
print(questionObj.getQuestionProperties())
