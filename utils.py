import json














# funçoes do .json
def createData():
    data = {
        "Players": [],
    }

    with open("players.json", "w") as f:
        f.write(json.dumps(data, indent=1))

def readData():
    try:
        with open("players.json", "r") as f:
            data = json.loads(f.read())
            return data

    except FileNotFoundError:
        return False