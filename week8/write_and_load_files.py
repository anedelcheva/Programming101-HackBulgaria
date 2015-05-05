import json


def writeToFile(filename, text):
    with open(filename, 'w') as f:
        f.write(text)

def loadFromFile(filename):
    with open(filename, 'r') as f:
        text = f.read()
        to_json = json.loads(text)
        return to_json
