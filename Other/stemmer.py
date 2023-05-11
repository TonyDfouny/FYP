from snowballstemmer import stemmer

ar_stemmer = stemmer("arabic")
en_stemmer = stemmer("english")
print(en_stemmer.stemWord('found'))
import nltk
from nltk.stem import PorterStemmer

ps = PorterStemmer()
print(ps.stem('ate'))



sno = nltk.stem.SnowballStemmer('english')
print(sno.stem('ate'))
