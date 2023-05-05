import DB
def DBwordFinder(word):
    """
    :param word: 'arword'
    :return: 'phoeword' from DB
    """
    return DB.ArPhoeDB[word]

def DBverbFinder(verb,person):
    """
    :param verb: 'arverb'
    :param person: 'person'
    :return: the corresponding 'phoeverb'
    """

    return DB.VerbDB[verb][person]