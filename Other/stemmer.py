from snowballstemmer import stemmer

ar_stemmer = stemmer("arabic")
en_stemmer = stemmer("english")
print(en_stemmer.stemWord('sleeping'))
