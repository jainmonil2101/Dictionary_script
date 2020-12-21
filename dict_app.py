import json
from difflib import *
data = json.load(open('data.json'))


monil = get_close_matches('rainn', data.keys())[0]



def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        monil = input(f'Do you mean {get_close_matches(w, data.keys())[0]} instead? Enter \'Y\' for Yes or \'N\' for No: ')
        if monil == 'y' or monil == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif monil == 'n' or monil == 'N':
            return 'Please try again.'
        else:
            return 'we didn\'t understand your entry. Please double check it.'
        
    else:
        return 'The word doesn\'t exist. Please double check it.'

word = input('Enter a word: ')
result = translate(word)
if type(result) == list and len(result) > 1:
    for index, i in enumerate(result, 1):
        print(f"{index}. {i}")
else:
    print(''.join(result))