import json


def read_json(filename):
    filepath = "../data/" + filename
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
