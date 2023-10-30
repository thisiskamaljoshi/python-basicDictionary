import json

data = json.load(open("dict_data.json"))

def meaning(word):
    word=word.lower()
    if(word in data):
        return data[word]
    else:
        return ["Word Doesnt Exist In Dictionary"]

word =input("Enter Word:")

meanings= meaning(word)

for meaning in meanings:
    print(meaning)

