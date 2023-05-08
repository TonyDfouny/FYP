#PARSER#
import ArabicParser,VerbTranslator,Finder,ALwordsTranslator
from EngArTranslator import *

def ArPhoeTranslator(sourcesentence):
    """

    :param sourcesentence: 'sentence english'
    :return: 'sentence in phoenician'
    """
    # TRANSLATE FROM ENGLISH TO ARABIC#
    translatedsentence = TranslateOffline(sourcesentence)
    # print('offline: ',translatedsentence)
    #
    # translatedsentence=TranslateOnline(sourcesentence)
    # print('online: ',translatedsentence)

    parsedsentence=ArabicParser.ArabicParser(translatedsentence)

    output_sentence=''
    for words in parsedsentence:
        if words[0]=='V':
            #word = words.split()[1]
            output_sentence=output_sentence+' '+VerbTranslator.VerbTranslator(words)
        elif words[:2]=='DT':
            output_sentence=output_sentence+' '+ALwordsTranslator.Alwords(words)
        else:
            word=words.split()[1]
            output_sentence=output_sentence+' '+Finder.FindWord(word)


    return output_sentence

########TEST###########
# translatedsentence='هو يأتي مع ابن الى بيروت'
# print(ArPhoeTranslator(translatedsentence))