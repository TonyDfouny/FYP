from snowballstemmer import stemmer

ar_stemmer = stemmer("arabic")
print(ar_stemmer.stemWord(u'أَكَلْنَا'))