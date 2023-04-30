#PARSER#
from ArabicParser import *
from VerbTranslator import *
import DB


def ArPhoeTranslator(sourcesentence):
    """

    :param sourcesentence: 'sentence in arabic'
    :return: 'sentence in phoenician'
    """
    parsedsentence=ArabicParser(sourcesentence)
    output_sentence=''
    for words in parsedsentence:
        if words[0]=='V':
            #word = words.split()[1]
            output_sentence=output_sentence+' '+VerbTranslator(words)
        else:
            word=words.split()[1]
            output_sentence=output_sentence+' '+DB.ArPhoeDB[word]


    return output_sentence

########TEST###########
# translatedsentence='هو يأتي مع ابن الى بيروت'
# print(ArPhoeTranslator(translatedsentence))