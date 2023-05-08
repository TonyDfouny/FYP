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
    try:
        suffix[0]
        suffix[1]
        try:
            phoeword=WordFinder.DBwordFinder(suffix[0])
            return phoeword + Posdict[suffix[1]]
        except KeyError:
            raise KeyError
    except IndexError:
        raise KeyError



