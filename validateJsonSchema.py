import json
from jsonschema import validate, exceptions

questions = ".\questionsInput.json"
questions = json.load(open(questions))

jsonSchema = ".\jsonSchema.json"
jsonSchema = json.load(open(jsonSchema))

try:
    validate(questions, jsonSchema)
except exceptions.ValidationError as err:
    print(err.message)
