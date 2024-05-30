import requests
URL = "https://raw.githubusercontent.com/epshteinmatthew/cesiumscalabilitytest/main/metadata.json"

def lookup(index):
    data = requests.get(url=URL).json()
    return requests.get(url = "https://raw.githubusercontent.com/epshteinmatthew/cesiumscalabilitytest/main/" + data[index.__str__()]).content

def lookup_range(lower, upper):
    data = requests.get(url=URL).json()
    list = [item[1] for item in data.items() if int(item[0]) <= upper and int(item[0]) >= lower]
    return [ requests.get(url = "https://raw.githubusercontent.com/epshteinmatthew/cesiumscalabilitytest/main/" + item).content for item in list]

print(lookup_range(123, 1240))