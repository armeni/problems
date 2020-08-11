import json
from core.emoji import *

def info(s):
    native = capital = curr = ph = ' '
    lang = list()
    data = 'data/info.json'
    with open(data, 'r') as f:
        db = json.load(f)
        for i in db:
            if s == i["name"]:
                native = i["native"] + ")\n"
                capital = cap + 'Capital: ' + i["capital"] + "\n"
                lang = language + 'Official languages: ' + converter(i["languages"]) + "\n"
                curr = currency + 'Currency: ' + i["currency"] + "\n"
                ph = phone + 'Calling code: ' + i["phone"] + "\n"
    if native == ' ':
        return 'There is no such country! Perhaps you were mistaken!'
    else:
        return flag_emoji(s) + s + " (" + native + capital + lang + curr + ph

def converter(t):
    data = 'data/languages.json'
    l = ' '
    with open(data, 'r') as h:
        db = json.load(h)
        for j in t:
            for key in db.keys():
                if j==key:
                    l = l + ', ' + str(db[key]["name"])
    return l[3:]

def flag_emoji(s):
    data = 'data/flagemoji.json'
    with open(data, 'r') as g:
        db = json.load(g)
        for i in db:
            if s == i["name"]:
                f = i["emoji"]
    return f