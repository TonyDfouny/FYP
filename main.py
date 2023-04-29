from EngArTranslator import *
#from Arabic import *
sourcesentence='I am eating'

translatedsentence = TranslateOffline(sourcesentence)
print(translatedsentence)
# translatedsentence=TranslateOnline(sourcesentence)
# print(translatedsentence)

# parsedsentence=ArabicParser(translatedsentence)
# print(parsedsentence)