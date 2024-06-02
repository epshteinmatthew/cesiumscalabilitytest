import json
import os
import sys


def lookup(index):
    data = json.loads(open("metadata.json", "r").read())
    return open(os.getcwd() + "/" + data[index.__str__()]).read()

print(lookup(int(sys.argv[1])))
