import json
from jsonschema import validate, exceptions

schema = json.load(open("jsonSchema.json"))

questions = json.load(open("..\questionsInput.json"))

try:
    validate(questions, schema)
    print("")
    print("//////////////////////////////////////////")
    print("--> Correct Question Format")
    print("//////////////////////////////////////////")
    print("")

except exceptions.ValidationError as err:
    print("")
    print("//////////////////////////////////////////")
    print(err.message)
    print("//////////////////////////////////////////")
    print("")