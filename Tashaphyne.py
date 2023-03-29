from tashaphyne.stemming import ArabicLightStemmer

ArListem = ArabicLightStemmer()
#word ='يأكلون'
# word='يَأكُلُونَ'
# # stemming word
# stem = ArListem.light_stem(word)
# # extract stem
# print(ArListem.get_stem())
# # extract root
# print(ArListem.get_prefix())
# print(ArListem.get_suffix())

#words=['آكُلُ','تَأكُلُ','تَأكُلِينَ','يَأكُلُ','تَأكُلُ','نَأكُلُ','تَأكُلُونَ','تَأكُلنَ','يَأكُلُونَ','يَأكُلنَ','تَأكُلَانِ','يَأكُلَانِ','تَأكُلَانِ']
words=['آكل','تأكل','تأكلين','يأكل','تأكل','نأكل','تأكلون','تأكلن','يأكلون','يأكلن','تأكلان','يأكلان','تأكلان']
for word in words:
    print(word)
    ArListem.light_stem(word)
    print(ArListem.get_prefix())
    print(ArListem.get_suffix())