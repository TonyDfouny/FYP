import WordFinder

def FindWord(word,translationtype):
    """

    :param word: 'arword'
    :return: 'phoeword'
    """
    from nltk.stem import arlstem2
    import PossesivewordsTranslator
    stemmer = arlstem2.ARLSTem2()
    try:
        return WordFinder.DBwordFinder(word,translationtype)
    except KeyError:
        try: #If possessive 'ابنه','ابنها','إبنهم','إبنك'
            return PossesivewordsTranslator.Possesive(word,translationtype)
        except KeyError:
            try:
                return WordFinder.DBwordFinder(stemmer.stem(word),translationtype)
            except KeyError:
                # try:
                #     return SynonymFinder.Synonym(word)
                # except KeyError:
                    return word



#print(FindVerb('اتي','1p.s.c.'))
#print (FindWord('ابنه'))

def FindVerb(verb,rootverb,translationtype):
    """
    :param verb: 'verb' original verb in arabic (as translated)
    :param rootverb: 'rootverb' of the original verb in arabic
    :param translationtype: 'online or offline'
    :return: 'verb in phoe'
    """
    #get translated verb where dict[rootverb] and person[person]
    from nltk.stem import arlstem2
    stemmer = arlstem2.ARLSTem2()
    try:
        return WordFinder.DBverbFinder(rootverb,translationtype)
    #If nothing is found we try with a stemed verb
    except KeyError:
        try:
            return WordFinder.DBverbFinder(stemmer.stem(rootverb),translationtype)
        except KeyError:
            try:
                return WordFinder.DBverbFinder(verb,translationtype)
            except KeyError:
                try:
                    return WordFinder.DBverbFinder(stemmer.stem(verb),translationtype)
                except KeyError:
                    phoe=FindWord(rootverb,translationtype)
                    if phoe==rootverb:
                        return FindWord(verb,translationtype)
                    else:
                        return phoe



#print(FindVerb('أجمع','person'))