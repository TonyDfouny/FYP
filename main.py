import sys

sys.path.append(str(r"C:\Users\tony_\Desktop\temp\ESIB\FYP\Translator\EngArPhoe"))
sys.path.append(str(r"C:\Users\tony_\Desktop\temp\ESIB\FYP\Translator\Database"))
sys.path.append(str(r"C:\Users\tony_\Desktop\temp\ESIB\FYP\Translator\EngPhoe"))
sys.path.append(str(r"C:\Users\tony_\Desktop\temp\ESIB\FYP\Translator\PhoeEng"))
#print(sys.path)
from GUI.GUI import *

LanguageTranslator()

# import EngPhoeTranslator
#
# print(EngPhoeTranslator.EngPhoeTranslator('I say').Translate())

# from EngArPhoe import ArPhoeTranslator
#
# print(ArPhoeTranslator.ArPhoeTranslator('eat','Offline'))

