from tashaphyne.stemming import ArabicLightStemmer

# ArListem = ArabicLightStemmer()
# word ='أمش'
# # word='يَأكُلُونَ'
# # # stemming word
# stem = ArListem.light_stem(word)
# # # extract stem
# print(ArListem.get_stem())
# # # extract root
# # print(ArListem.get_prefix())
# # print(ArListem.get_suffix())
# t=(ArListem.get_prefix(),ArListem.get_suffix())
# #t=(ArListem.get_suffix(),ArListem.get_prefix())
# print(t)

#words=['آكُلُ','تَأكُلُ','تَأكُلِينَ','يَأكُلُ','تَأكُلُ','نَأكُلُ','تَأكُلُونَ','تَأكُلنَ','يَأكُلُونَ','يَأكُلنَ','تَأكُلَانِ','يَأكُلَانِ','تَأكُلَانِ']
# words=['آكل','تأكل','تأكلين','يأكل','تأكل','نأكل','تأكلون','تأكلن','يأكلون','يأكلن','تأكلان','يأكلان','تأكلان']
# for word in words:
#     print(word)
#     ArListem.light_stem(word)
#     print(ArListem.get_prefix())
#     print(ArListem.get_suffix())

# import nltk
# from nltk.stem.isri import ISRIStemmer
# st = ISRIStemmer()
# w= 'أمشي'
# w2='ألعب'
# print(st.stem(w2))

from nltk.stem import arlstem2

stemmer=arlstem2.ARLSTem2()

#word = stemmer.stem('يعمل')
# verb='يعمل'
# w2='تلعب'
# w3='تأكل'
# t=stemmer.norm(w3)
# print(t)
# word=stemmer.verb(w3)
# print(word)

presentverbs=['آكل','تأكل','تأكلين','يأكل','تأكل','نأكل','تأكلون','تأكلن','يأكلون','يأكلن','تأكلان','يأكلان','تأكلان','ألعب','أأكل']
pastverb=['أَكَلتُ','أَكَلتَ','أَكَلتِ','أَكَلَ','أَكَلَت','أَكَلنَا','أَكَلتُم','أَكَلتُنَّ','أَكَلُوا','أَكَلنَ','أَكَلتُمَا','أَكَلَا','أَكَلَتَا']
for vern in presentverbs:
    print(verb)
    #print(stemmer.verb(word))
    print(stemmer.verb(stemmer.norm(verb))[1:])
    #print(stemmer.presentverb(stemmer.norm(word)))
    #print(stemmer.verb_t1(stemmer.norm(word)))


""" آكل false translation lezim tkoun أأكل"""