import DB
def DBwordFinder(word):

    return DB.ArPhoeDB[word]

def DBverbFinder(verb,person):

    return DB.VerbDB[verb][person]