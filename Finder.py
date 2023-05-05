import DB
import WordFinder

def FindVerb(rootverb,person):
    """

    :param rootverb: 'rootverb' of the original verb in arabic
    :param person:  'person'
    :return: 'verb in phoe'
    """
    try:    #get translated verb where dict[rootverb] and person[person]
        rootphoeverb=WordFinder.DBwordFinder(rootverb)
        phoeverb=WordFinder.DBverbFinder(rootphoeverb,person)
        #print('root =',rootverb,'\n',person)
        return phoeverb
    except KeyError:
        return rootverb




def FindWord(word):
    """

    :param word: 'arword'
    :return: 'phoeword'
    """
    from nltk.stem import arlstem2
    import PossesivewordsTranslator,SynonymFinder
    stemmer = arlstem2.ARLSTem2()
    try:
        return WordFinder.DBwordFinder(word)
    except KeyError:
        try: #If possessive 'ابنه','ابنها','إبنهم','إبنك'
            return PossesivewordsTranslator.Possesive(word)
        except KeyError:
            try:
                return WordFinder.DBwordFinder(stemmer.stem(word))
            except KeyError:
                try:
                    return SynonymFinder.Synonym(word)
                except KeyError:
                    return word



#print(FindVerb('اتي','1p.s.c.'))
#print (FindWord('ابنه'))