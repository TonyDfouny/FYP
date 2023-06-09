import json
import sys
class PhoeWordFinder():
    def __init__(self,word):
        """
        :param word: 'word in phoe'
        """
        self.word=word
    def __Finder(self):
        """

        :return: word in english or none
        """
        words = open(sys.path[1]+r'\Database\DATABASE.json', 'r', encoding='utf-8')
        wordsDB = json.load(words)
        words.close()
        for line in wordsDB:
            if self.word == line['Transcript']:
                return line['English'].split(',')[0]

    def WordFinder(self):
        """

        :return: word in english
        """
        engword=self.__Finder()
        if engword is None:
            raise KeyError
        else:
            return engword

    def __Verb(self):
        """

        :return: verb in english or none
        """
        words = open(sys.path[1]+r'\Database\VERBDATABASE.json', 'r', encoding='utf-8')
        verbsDB = json.load(words)
        words.close()
        for line in verbsDB:
            if self.word == line['root_t']:
                return line['English'].split(',')[0]

    def VerbFinder(self):
        """

        :return: verb in english
        """
        engverb=self.__Verb()
        if engverb is None:
            raise KeyError
        else:
            return engverb