from tashaphyne.stemming import ArabicLightStemmer

ArListem = ArabicLightStemmer()
word = u'يأكلون'
# stemming word
stem = ArListem.light_stem(word)
# extract stem
print(ArListem.get_stem())
# extract root
print(ArListem.get_prefix())
print(ArListem.get_suffix())
