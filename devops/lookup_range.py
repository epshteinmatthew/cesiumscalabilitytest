import os, json
import sys


def lookup_range(lower, upper):
    data = json.loads(open("metadata.json", "r").read())
    list = [item[1] for item in data.items() if int(item[0]) <= upper and int(item[0]) >= lower]
    output = "files="
    for item in list:
        output += item
        output += "\n"
    print(output)



if sys.argv[3] == "1":
    (lookup_range(int(sys.argv[1]),int(sys.argv[2])))
else:
    filenames = sys.argv[4].splitlines()
    print([open(item, "r").read() for item in filenames])



