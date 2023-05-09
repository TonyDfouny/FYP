import json

def WordFinder(word):
    words = open('DATABASE.json', 'r', encoding='utf-8')
    wordsDB = json.load(words)
    for line in wordsDB:
        if word == line['Transcript']:
            return line['English'].split(',')[0]

def Finder(word):
    engword=WordFinder(word)
    if engword is None:
        raise KeyError
    else:
        return engword

def VerbFinder(word):
    words = open('VERBDATABASE.json', 'r', encoding='utf-8')
    verbsDB = json.load(words)
    for line in verbsDB:
        if word == line['root_t']:
            return line['English'].split(',')[0]

def Verb(word):
    engverb=VerbFinder(word)
    if engverb is None:
        raise KeyError
    else:
        return engverb