import json
import sys
class WordFinder:
    def __init__(self,word,translationtype):
        """

        :param word: 'arword' or 'verb in arabic'(root and stemmed)
        :param translationtype: 'Online' or 'Offline'
        """
        self.word=word
        self.translationtype=translationtype

    def __wordFinder(self):
        words = open(sys.path[1]+r'\Database\DATABASE.json', 'r', encoding='utf-8')
        wordsDB = json.load(words)
        words.close()
        if self.translationtype == 'Offline':
            for line in wordsDB:
                # if line['Stemmed Offline']==word:
                #     return line['Transcript']
                if self.word in line['Stemmed Offline'].split(','):
                    return line['Transcript']
        else:
            for line in wordsDB:
                # if line['Stemmed Online']==word:
                #     return line['Transcript']
                if self.word in line['Stemmed Online'].split(','):
                    return line['Transcript']
    def DBwordFinder(self):
        """
        :return: 'phoeword' from DB
        """
        if self.__wordFinder() is None:
            raise KeyError
        else:
            return self.__wordFinder()


    def __verbFinder(self):
        verbs = open(sys.path[1]+r'\Database\VERBDATABASE.json', 'r', encoding='utf-8')
        verbsDB = json.load(verbs)
        verbs.close()
        if self.translationtype=='Offline':
            for line in verbsDB:
                # if line['Stemmed Offline'] == verb:
                #     return line['Transcript']
                    # return line['Grammar'][person]
                if self.word in line['Stemmed Offline'].split(','):
                    if line['root_t'] != '':
                        return line['root_t']
        else:
            for line in verbsDB:
                # if line['Stemmed Offline'] == verb:
                #     return line['Transcript']
                    # return line['Grammar'][person]
                if self.word in line['Stemmed Online'].split(','):
                    if line['root_t'] != '':
                        return line['root_t']
    def DBverbFinder(self):
        """
        :return: the corresponding 'phoeverb'
        """
        if self.__verbFinder() is None:
            raise KeyError
        else:
            return self.__verbFinder()

