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

##TRY IT TO MAKE PROG WORK ON ANY PC##
from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).parent.parent

import os
ROOT_DIR = os.path.abspath(os.curdir)

import sys
print(sys.path[1])