import json
import difflib
from difflib import get_close_matches
data = json.load(open("dict_data.json"))

def meaning(word):
    word_lowercase=word.lower()

    if(word_lowercase in data):
        return data[word_lowercase]
    else:
        closestWord = get_close_matches(word_lowercase,data.keys(),n=1,cutoff=0.8)
        wordCheck="n"
        if(len(closestWord) >0):
            wordCheck= input("Cannot find {}. \nDid you mean {} instead? (Y/N)  ".format(word,closestWord[0])).lower()
        if(wordCheck == "y"):
            return data[closestWord[0]]
        else:    
            return ["The word doesnt exist in dictionary"]

word =input("Enter Word: ")

meanings= meaning(word)

for meaning in meanings:
    print(meaning)

