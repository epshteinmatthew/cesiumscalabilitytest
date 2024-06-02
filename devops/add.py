import json
import os
import random


def add(filedata, id):
    metadata = json.loads(open("metadata.json", "r").read())
    if(metadata[str(id)] != None):
        print("Unable to add file, entry with ID" + str(id) + " already exists.")
        return False
    url = "file_" + (random.randint(1000000,2000000) * id).__str__()
    while(os.path.exists(url)):
        url += "_1"
    open(url, "x").write(filedata)
    metadata[str(id)] = url
    open("metadata.json", "w").write(json.dumps(metadata))
    print("File added at url "+url)
    return True

add("dyfhgjhkj;l'k;", 112435456758)



