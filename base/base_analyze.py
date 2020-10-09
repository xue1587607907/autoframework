import json


def analyze_data(filename):
    with open("./data/"+filename, "r", encoding="utf-8")as f:
        list_data = []
        data_dict = json.load(f)
        for value in data_dict.values():
            list_data.append(value)
        return list_data
