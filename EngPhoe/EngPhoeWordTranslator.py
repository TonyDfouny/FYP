import json

class EngPhoeWordTranslator:
    def __init__(self,word,allchildren):
        self.word=word[0]
        self.tag=word[1]
        self.dep=word[2]
        self.children=allchildren

    def __finder(self,word):
        words = open('Database\DATABASE.json', 'r', encoding='utf-8')
        wordsDB = json.load(words)

        for line in wordsDB:
            if word in line['English'].split(','):
                return line['Transcript']
    def __Finder(self,word):
        if self.__finder(word) is None:
            return word
        else:
            return self.__finder(word)


    def __Alword(self):
        phoeword=self.__Finder(self.word)
        if phoeword == self.word:
            return None
        else:
            return 'h'+phoeword

    def __Possessive(self,posspronoun):
        poss={
            'my':'y',
            'your':'k',
            'his':'h',
            'her':'h',
            'its': 'h',
            'our':'n',
            'their':'m'
        }

        phoeword = self.__Finder(self.word)
        if phoeword == self.word:
            return None
        else:
            return phoeword+poss[posspronoun.lower()]
    def __CheckTranslate(self):
        if len(self.children[self.word])==0:
            return None
        for child in self.children[self.word]:
            if child[2]=='poss':
                return self.__Possessive(child[0])
            elif child[2]=='det' and child[0].lower()=='the':
                return self.__Alword()

    def Translate(self):
        if self.__CheckTranslate() is None:
            raise KeyError
        else:
            return self.__CheckTranslate()