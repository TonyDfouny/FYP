import Finder

def Alwords(words):

    from nltk.stem import arlstem2
    """

    :param words: 'word TAG'
    :return: 'word in Phoenician with H instead of AL'
    """
    stemmer = arlstem2.ARLSTem2()
    word=words.split()[1]
    stemmedword=stemmer.pref(word)

    output='h'+Finder.FindWord(stemmedword)

    return output
