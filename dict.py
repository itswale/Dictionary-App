import json

#Library to get the word closest to a wrong word
from difflib import get_close_matches

#disctionary jason file
data = json.load(open("data.json"))

#Function takes a word and returns it's meanings. If word is wrong, lists closest word to the wrong word
def translate(w):
    w = w.lower()
    if w in data:
        return(data[w])
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Do you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w, data.keys())[0])
        if yn.upper() == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.upper() == "N":
            nw = input("What would you like to search: " )
            return (translate(nw))
        elif yn.upper != "Y" or "N":
            wrong = ("Wrong choice. ")
            return wrong
    else:
        return("Word does not exist, please check again. ")

word = input("Enter a word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
