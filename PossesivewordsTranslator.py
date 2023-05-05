def Possesive(word):
    """

    :param word: 'word' in arabic with possessive suffix
    :return: 'phoeword' with the corresponding possessive suffix
    """
    import WordFinder
    from nltk.stem import arlstem2
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
    return WordFinder.DBwordFinder(suffix[0])+Posdict[suffix[1]]
