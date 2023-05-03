
from nltk.stem import arlstem2

words=['ابنه','ابنها','إبنهم','إبنك','كلبنا','كلبكي','كلبكم']
stemmer = arlstem2.ARLSTem2()
#for word in words:
    ##print(stemmer.customsuff(stemmer.norm(word)) )#remove prefix and suffix
    #print(stemmer.customstem(word))
    ##print(stemmer.adjective(word))
# print(stemmer.pref('الحيوانات')) ##remove al
w='الحيوانات'
# print(stemmer.customstem(w))
# print(stemmer.pref(w))
# print(stemmer.custompref(w))
print(stemmer.stem('ابني'))
print(stemmer.stem('كلبي'))
# token='abcdefgh'
# print(token[1:-2] + token[-1])
# print(token[0]+token[-2])