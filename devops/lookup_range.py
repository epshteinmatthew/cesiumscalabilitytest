import os, json
import sys


def lookup_range(lower, upper):
    data = json.loads(open("metadata.json", "r").read())
    list = [item[1] for item in data.items() if int(item[0]) <= upper and int(item[0]) >= lower]
    return [  open(os.getcwd() + "/" + item).read() for item in list]

print(lookup_range(int(sys.argv[0]),int(sys.argv[1])))
