
from nltk.stem import arlstem2

words=['ابنه','ابنها','إبنهم','إبنك','كلبنا','كلبكي','كلبكم','كلبي']
stemmer = arlstem2.ARLSTem2()
print(stemmer.norm('كاهن'))
"""
customstemmer=arlstem2.CustomARLSTem2()
for word in words:
    #print(stemmer.customsuff(stemmer.norm(word)) )#remove prefix and suffix
    print(customstemmer.possessive(word))
    #print(stemmer.adjective(word))
# print(stemmer.pref('الحيوانات')) ##remove al
# w='الحيوانات'
# print(stemmer.customstem(w))
# print(stemmer.pref(w))
# print(stemmer.custompref(w))
# print(stemmer.stem('ابني'))
# print(customstemmer.possessive('كلبي'))
# print(customstemmer.suff('ابنه'))
# print(stemmer.pref('الحيوان'))
# token='abcdefgh'
# print(token[1:-2] + token[-1])
# print(token[0]+token[-2])
# L=[1,2,'sadsad']
# print(len(L))
"""
l=[1,3,4,6,7]
l.remove(4)
print(l)
n='tony'
print(n.count(' '))