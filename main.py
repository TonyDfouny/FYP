from Translator import *
from Arabic import *
sourcesentence='Tony Dfouny,the kids and I are sleeping'

translatedsentence = TranslateOffline(sourcesentence)
print(translatedsentence)

parsedsentence=ArabicParser(translatedsentence)
print(parsedsentence)