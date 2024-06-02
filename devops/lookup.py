import json
import os

def lookup(index):
    data = json.loads(open("metadata.json", "r").read())
    return open(os.getcwd() + "/" + data[index.__str__()]).read()

lookup(12)
