import nltk
from nltk import pos_tag, word_tokenize, RegexpParser
from nltk.corpus import treebank
sentence = """I built three houses"""

tokens = nltk.word_tokenize(sentence)
print("tokens = \n",tokens)

tagged = nltk.pos_tag(tokens)
print("tagged = \n",tagged[0:])

entities = nltk.chunk.ne_chunk(tagged)
print("entities = \n",entities)

chunker = RegexpParser("""
                    NP: {<DT>?<JJ>*<NN>} #To extract Noun Phrases
                    P: {<IN>}            #To extract Prepositions
                    V: {<V.*>}           #To extract Verbs
                    PP: {<p> <NP>}       #To extract Prepositional Phrases
                    VP: {<V> <NP|PP>*}   #To extract Verb Phrases
                    """)
output = chunker.parse(tagged)
print("Output = \n", output)
output.draw()

tagged = nltk.pos_tag(tokens)
print(tagged)

# t = treebank.parsed_sents('wsj_0001.mrg')[0]
# t.draw()