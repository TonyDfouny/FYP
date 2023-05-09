import json

words = open('DATABASE.json','r',encoding='utf-8')
wordsDB = json.load(words)

def wordFinder(word,translationtype):
    if translationtype == 'Offline':
        for line in wordsDB:
            # if line['Stemmed Offline']==word:
            #     return line['Transcript']
            if word in line['Stemmed Offline'].split(','):
                return line['Transcript']
    else:
        for line in wordsDB:
            # if line['Stemmed Offline']==word:
            #     return line['Transcript']
            if word in line['Stemmed Online'].split(','):
                return line['Transcript']
def DBwordFinder(word,translationtype):
    """
    :param word: 'arword'
    :return: 'phoeword' from DB
    """
    if wordFinder(word,translationtype) is None:
        raise KeyError
    else:
        return wordFinder(word,translationtype)

verbs=open('VERBDATABASE.json','r',encoding='utf-8')
verbsDB = json.load(verbs)



def verbFinder(verb,person,translationtype):
    if translationtype=='Offline':
        for line in verbsDB:
            # if line['Stemmed Offline'] == verb:
            #     return line['Transcript']
                # return line['Grammar'][person]
            if verb in line['Stemmed Offline'].split(','):
                return line['Transcript']
    else:
        for line in verbsDB:
            # if line['Stemmed Offline'] == verb:
            #     return line['Transcript']
                # return line['Grammar'][person]
            if verb in line['Stemmed Online'].split(','):
                return line['Transcript']
def DBverbFinder(verb,person,translationtype):
    """
    :param verb: 'verb in arabic'
    :param person: 'person'
    :return: the corresponding 'phoeverb'
    """
    if verbFinder(verb,person,translationtype) is None:
        raise KeyError
    else:
        return verbFinder(verb,person,translationtype)

