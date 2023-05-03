import DB
from nltk.stem import arlstem2

import PossesivewordsTranslator

stemmer = arlstem2.ARLSTem2()

def FindVerb(rootverb,person):
    """

    :param rootverb: 'rootverb' of the original verb in arabic
    :param person:  'person'
    :return: 'verb in phoe'
    """
    try:    #get translated verb where dict[rootverb] and person[person]
        infphoeverb=DB.ArPhoeDB[rootverb]
        phoeverb=DB.VerbDB[infphoeverb][person]
        #print('root =',rootverb,'\n',person)
    except KeyError:
        return rootverb

    return phoeverb

def DBwordFinder(word):
    return DB.ArPhoeDB[word]
def FindWord(word):
    """

    :param word: word in arabic
    :return: word in phoenician
    """
    try:
        return DBwordFinder(word)
    except KeyError:
        try: #If possessive 'ابنه','ابنها','إبنهم','إبنك'
            return PossesivewordsTranslator.Possesive(word)
        except KeyError:
            try:
                return DBwordFinder(stemmer.stem(word))
            except KeyError:
                return word



#print(FindVerb('اتي','1p.s.c.'))
#print (FindWord('ابنه'))