import json

JSON_PATH = "config.json"

def saveJson(data, file=JSON_PATH):
    with open(file, 'w') as f:
        json.dump(data, f)
    
def loadJson(file=JSON_PATH):
    with open(file, 'r') as f:
        return json.load(f)

