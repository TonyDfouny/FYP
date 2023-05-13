#PARSER#
import ArabicParser,VerbTranslator,Finder,ALwordsTranslator
import EngArTranslator
from EngPhoe import EngPhoeTranslator


def ArPhoeTranslator(sourcesentence,translationtype):
    """

    :param sourcesentence: 'sentence english'
    :param translationtype: 'online or offline'
    :return: 'sentence in phoenician'
    """
    # TRANSLATE FROM ENGLISH TO ARABIC#

    translator= EngArTranslator.Translator(sourcesentence, 'en', 'ar', translationtype)
    translatedsentence=translator.Translate()

    parsedsentence= ArabicParser.ArabicParser(translatedsentence)

    output_sentence=''
    for words in parsedsentence:
        word=words.split()[1]
        if words[0]=='V':
            newword= VerbTranslator.VerbTranslator(words, translationtype).Translate()
            if newword==word:
                engword= EngArTranslator.Translator('هو '+word, 'ar', 'en', 'Online').Translate()
                engverb=engword.split()[-1]
                output_sentence = output_sentence + ' ' + EngPhoeTranslator.EngPhoeTranslator(engverb).Translate()
            else:
                output_sentence=output_sentence+' '+newword
            #output_sentence = output_sentence+' '+VerbTranslator.VerbTranslator(words,translationtype).Translate()
        elif words[:2]=='DT':
            newword = ALwordsTranslator.Alwords(words, translationtype)
            if newword == word:
                engword = EngArTranslator.Translator(word, 'ar', 'en', 'Online').Translate()

                output_sentence = output_sentence + ' ' + EngPhoeTranslator.EngPhoeTranslator(engword).Translate()
            else:
                output_sentence = output_sentence + ' ' + newword
            #output_sentence=output_sentence+' '+ALwordsTranslator.Alwords(words,translationtype)
        else:
            newword= Finder.FindWord(word, translationtype)
            if newword == word:
                engword = EngArTranslator.Translator(word, 'ar', 'en', 'Online').Translate()
                output_sentence = output_sentence + ' ' + EngPhoeTranslator.EngPhoeTranslator(engword).Translate()
            else:
                output_sentence = output_sentence + ' ' + newword
            #output_sentence=output_sentence+' '+Finder.FindWord(word,translationtype)


    return output_sentence

########TEST###########
# translatedsentence='هو يأتي مع ابن الى بيروت'
#print(ArPhoeTranslator('he eat','Offline'))
#print(ArPhoeTranslator('he eat','Online'))