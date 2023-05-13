import json
import spacy
import EngPhoeWordTranslator
import EngPhoeVerbTranslator

nlp = spacy.load("en_core_web_sm")
from snowballstemmer import stemmer
en_stemmer = stemmer("english")
class EngPhoeTranslator:
    def __init__(self,sourcesentence):
        """

        :param word: word in english
        """
        self.sourcesentence=sourcesentence

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
    # def __verbfinder(self,rootverb):
    #     verbs = open('VERBDATABASE.json', 'r', encoding='utf-8')
    #     verbsDB = json.load(verbs)
    #
    #     for line in verbsDB:
    #         if rootverb in line['English'].split(','):
    #             return line['root_t']
    # def __VerbFinder(self,rootverb):
    #     if self.__verbfinder(rootverb) is None:
    #         return rootverb
    #     else:
    #         return self.__verbfinder(rootverb)
    # def SpacyParser(sourcesentence):
    #     parsedsentence=[]
    #     for token in nlp(sourcesentence):
    #         parsedsentence.append([token,token.tag_])
    #     return parsedsentence

    def Translate(self):
        parsedsentence = []
        allchildren = {}
        for token in nlp(self.sourcesentence):
            parsedsentence.append([str(token), str(token.tag_), str(token.dep_)])
            allchildren[str(token)] = []
            # allchildren[str(token)].append('hi')
            for child in token.children:
                if str(token) in allchildren.keys():
                    allchildren[str(token)].append(([str(child.text), str(child.tag_), str(child.dep_)]))
                else:
                    allchildren[str(token)] = [str(child.text), str(child.tag_), str(child.dep_)]
        #print('all',allchildren)
        outputsentence=''
        for parsedword in parsedsentence:
            word=parsedword[0]
            if parsedword[1][0]=='V' and parsedword[2]!='aux':
                try:
                    outputsentence = outputsentence +' ' + EngPhoeVerbTranslator.EngPhoeVerbTranslator(parsedword, allchildren).Translate()
                except KeyError:
                    outputsentence = outputsentence + ' ' + self.__Finder(str(word))
            elif parsedword[1][0]=='V' and parsedword[2]=='aux':
                outputsentence=outputsentence
            elif parsedword[2]=='det' or parsedword[2]=='poss':
                outputsentence = outputsentence
            else:
                try:

                    outputsentence= outputsentence +' ' + EngPhoeWordTranslator.EngPhoeWordTranslator(parsedword, allchildren).Translate()
                except KeyError:
                    outputsentence = outputsentence +' '+self.__Finder(str(word))

        return outputsentence

#print(EngPhoeTranslator('the silver').Translate())
#print(Finder('King'))
# parsedsentence = []
# for token in nlp('his son'):
#     parsedsentence.append([token, token.tag_])