import json

data = json.load(open("dict_data.json"))

def meaning(word):
    if(word in data):
        return data[word]
    else:
        return ["No Word Found"]

meanings =meaning("rn")

for meaning in meanings:
    print(meaning)

