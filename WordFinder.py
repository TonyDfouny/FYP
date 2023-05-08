import json

words = open('DATABASE.json','r',encoding='utf-8')
wordsDB = json.load(words)

def wordFinder(word):
    for line in wordsDB:
        if line['Stemmed Offline']==word:
            return line['Transcript']
def DBwordFinder(word):
    """
    :param word: 'arword'
    :return: 'phoeword' from DB
    """
    if wordFinder(word) is None:
        raise KeyError
    else:
        return wordFinder(word)

verbs=open('VERBDATABASE.json','r',encoding='utf-8')
verbsDB = json.load(verbs)



def verbFinder(verb,person):
    for line in verbsDB:
        if line['Stemmed Offline'] == verb:
            return line['Transcript']
            # return line['Grammar'][person]
def DBverbFinder(verb,person):
    """
    :param verb: 'verb in arabic'
    :param person: 'person'
    :return: the corresponding 'phoeverb'
    """
    if verbFinder(verb,person) is None:
        raise KeyError
    else:
        return verbFinder(verb,person)

