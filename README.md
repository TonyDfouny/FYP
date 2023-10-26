# FYP

Token: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

#Try first:
pip install -r requirements.txt
nltk.download()

#In case of problems
pip install nltk (pip3 for mac)
nltk.download()
https://www.nltk.org/data.html

stanford packages links:
https://nlp.stanford.edu/software/lex-parser.shtml
download parser and arabic model


pip install spacy
spacy download en_core_web_sm


pip install Tashaphyne

pip install snowballstemmer

pip install ar-corrector
pip install pandas

pip install urbans

pip install --upgrade translators

pip install argostranslate
next step run this program to install en to ar:
############################
import argostranslate.package
import argostranslate.translate

from_code = "en"
to_code = "ar"

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
available_package = list(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)[0]
download_path = available_package.download()
argostranslate.package.install_from_path(download_path)
##################################################

###CORRECTORS###
pip install Caribe


###ARLSTEM2####
COPY THE CONTENT OF ARLSTEM2 IN C:\Users\(username)\AppData\Local\Programs\Python\Python310\Lib\site-packages\nltk\stem\arlstem2.py

###GUI###
pip install ttkbootstrap pyttsx3 pyperclip


