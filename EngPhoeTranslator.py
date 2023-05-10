import json
import spacy
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
        words = open('DATABASE.json', 'r', encoding='utf-8')
        wordsDB = json.load(words)

        for line in wordsDB:
            if word in line['English'].split(','):
                return line['Transcript']
    def __Finder(self,word):
        if self.__finder(word) is None:
            return word
        else:
            return self.__finder(word)
    def __verbfinder(self,rootverb):
        verbs = open('VERBDATABASE.json', 'r', encoding='utf-8')
        verbsDB = json.load(verbs)

        for line in verbsDB:
            if rootverb in line['English'].split(','):
                return line['root_t']
    def __VerbFinder(self,rootverb):
        if self.__verbfinder(rootverb) is None:
            return rootverb
        else:
            return self.__verbfinder(rootverb)
    # def SpacyParser(sourcesentence):
    #     parsedsentence=[]
    #     for token in nlp(sourcesentence):
    #         parsedsentence.append([token,token.tag_])
    #     return parsedsentence

    def Translate(self):
        parsedsentence = []
        for token in nlp(self.sourcesentence):
            parsedsentence.append([token, token.tag_])
        outputsentence=''
        for parsedword in parsedsentence:
            word=parsedword[0]
            if parsedword[1][0]=='V':
                rootverb=en_stemmer.stemWord(str(word))
                outputsentence =outputsentence+' '+self.__VerbFinder(rootverb)
            else:
                outputsentence = outputsentence +' '+self.__Finder(str(word))

        return outputsentence
#print(EngPhoeTranslator('He eat').Translate())
#print(Finder('King'))
# parsedsentence = []
# for token in nlp('his son'):
#     parsedsentence.append([token, token.tag_])