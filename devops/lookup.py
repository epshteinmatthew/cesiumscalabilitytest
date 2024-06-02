import json
import os
import sys


def lookup(index):
    data = json.loads(open("metadata.json", "r").read())
    return open(os.getcwd() + "/" + data[index.__str__()]).read()

lookup(int(sys.argv[0]))
