import json
import spacy
nlp = spacy.load("en_core_web_sm")
from snowballstemmer import stemmer
en_stemmer = stemmer("english")

def finder(word):
    words = open('DATABASE.json', 'r', encoding='utf-8')
    wordsDB = json.load(words)

    for line in wordsDB:
        if word in line['English'].split(','):
            return line['Transcript']
def Finder(word):
    if finder(word) is None:
        return word
    else:
        return finder(word)
def SpacyParser(sourcesentence):
    parsedsentence=[]
    for token in nlp(sourcesentence):
        parsedsentence.append([token,token.tag_])
    return parsedsentence

def EngPhoeTranslator(sourcesentence):
    parsedsentence = []
    for token in nlp(sourcesentence):
        parsedsentence.append([token, token.tag_])
    outputsentence=''
    print(parsedsentence)
    for parsedword in parsedsentence:
        print(parsedword)
        word=parsedword[0]
        print(word)
        # if parsedword[1][0]=='V':
        #     rootverb=en_stemmer.stemWord(parsedword[0])
        #     print(rootverb)
        #     outputsentence =outputsentence+' ' +Finder(rootverb)
        # else:
        #     print(parsedword[0])
        #     #Finder(parsedword[0])
        #     outputsentence = outputsentence + ' ' +Finder(parsedword[0])
        #outputsentence = outputsentence + ' ' + Finder(parsedword[0])

print(EngPhoeTranslator('his son'))
#print(Finder('King'))