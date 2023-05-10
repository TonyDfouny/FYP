def Possesive(word,translationtype):
    """

    :param word: 'word' in arabic with possessive suffix
    :return: 'phoeword' with the corresponding possessive suffix
    """
    import WordFinder
    from nltk.stem import arlstem2
    stemmer=arlstem2.ARLSTem2()
    customstemmer = arlstem2.CustomARLSTem2()
    Posdict={'ي':'y',
     'ك':'k',
     'كي':'k',
     'ه': 'h',
     'ها': 'h',
     'نا':'n',
     'كم':'km',
     'هم':'m'
     }

    suffix = customstemmer.possessive(word)
    #
    # print(suffix[0][:-1]+'ة')
    try:
        if type(suffix) != list:
            raise IndexError
        if suffix[0][-1]=='ت':
            suffix[0]=suffix[0][:-1]+'ة'
        try:
            phoeword=WordFinder.WordFinder(suffix[0],translationtype).DBwordFinder()
            return phoeword + Posdict[suffix[1]]
        except KeyError:
            raise KeyError
    except IndexError:
        if suffix[-1]=='ي':
            try:
                phoeword = WordFinder.WordFinder(suffix[:-1], translationtype).DBwordFinder()
                return phoeword + Posdict['ي']
            except KeyError:
                raise KeyError
        else:
            raise KeyError

#print(Possesive('شمسه','Offline'))
#print(Possesive('ابني','Online'))
#print(Possesive('m','Online'))

