import json
import os


def delete(id):
    metadata = json.loads(open("metadata.json", "r").read())
    if(id.__str__() not in metadata):
        print("Unable to delete file, entry with ID" + str(id) + " does not exist.")
        return False
    os.remove(metadata[id.__str__()])
    del metadata[id.__str__()]
    open("metadata.json", "w").write(json.dumps(metadata))
    print("File with id "+ id.__str__() +" removed.")
    return True

delete(112435456758)