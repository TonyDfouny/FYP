
from nltk.stem import arlstem2

word='ابنه'
stemmer = arlstem2.ARLSTem2()
print(stemmer.stem(word)) #remove prefix and suffix
print(stemmer.pref('الحيوانات')) ##remove al

