from EngArTranslator import *
from ArPhoeTranslator import *

##########TRANSLATE FROM ENGLISH TO ARABIC###########

#sourcesentence=" I protect his sister from dangerous animals "
sourcesentence='He comes with son to Beirut'
translatedsentence = TranslateOffline(sourcesentence)
print('offline: ',translatedsentence)

translatedsentence=TranslateOnline(sourcesentence)
print('online: ',translatedsentence)



##########TRANSLATE FROM ARABIC TO PHOENICIAN#############
#translatedsentence='هو يأتي مع ابن الى بيروت'

print(ArPhoeTranslator(translatedsentence))