import sys

sys.path.append(sys.path[1]+r"\EngArPhoe")
sys.path.append(sys.path[1]+r"\Database")
sys.path.append(sys.path[1]+r"\EngPhoe")
sys.path.append(sys.path[1]+r"\PhoeEng")

from GUI.GUI import *

#LanguageTranslator()
#print(ArPhoeTranslator('They found the coffin','Offline'))
#print(ArPhoeTranslator('He is collecting the silver','Offline'))
print(EngPhoeTranslator.EngPhoeTranslator('I am collecting the silver in Byblos').Translate())