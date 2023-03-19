import nltk
from nltk import pos_tag, word_tokenize, RegexpParser
from nltk.corpus import treebank
sentence = """They are eating an apple and he is sleeping"""

tokens = nltk.word_tokenize(sentence)
print("tokens = \n",tokens)

tagged = nltk.pos_tag(tokens)
print("tagged = \n",tagged)
singular=['I','You','HE','SHE','IT']
plural=['WE','You','THEY']
def Customtag(tagged):
    liste=[]
    customlist=[]
    for i in tagged:
        if i[0].upper() in singular:
            liste=list(i)
            liste[1] = 'PRPS'
            customlist.append(liste)
        elif i[0].upper() in plural:
            liste = list(i)
            liste[1] = 'PRPP'
            customlist.append(liste)
        else:
            liste = list(i)
            customlist.append(liste)
    print('LIsteeeeee=',liste)
    return customlist
print('Custommmmm=',Customtag(tagged))
#print(('PRP') in tagged[0:][0:][0:])
#
# entities = nltk.chunk.ne_chunk(tagged)
# print("entities = \n",entities)


# Pronouns=[[word, tag] for word, tag in tagged if (tag=='PRP')]
# print('Pronouns = ',Pronouns)
#
# for i in Pronouns:
#     if i[0].upper() in singular:
#         i[1]='PRPS'
#     else:
#         i[1]='PRPP'
# print('Pronouns = ',Pronouns)
# for i in tagged:
#     if i[0].upper() in singular:
#         list(i)
#         i[1] = 'PRPS'
#     else:
#         list(i)
#         i[1] = 'PRPP'
# print("new tagged = \n",tagged)
# #
# # Extracting all Nouns from a text file using nltk
#
# for i in range(0,3):
#     token_comment = word_tokenize(comment[i])
#     tagged_comment = pos_tag(token_comment)
#     print( [(word, tag) for word, tag in tagged_comment if (tag=='NNP')])



# chunker = RegexpParser("""
#                     NP: {<DT>?<JJ>*<NN>} #To extract Noun Phrases
#                     P: {<IN>}            #To extract Prepositions
#                     V: {<V.*>}           #To extract Verbs
#                     PP: {<p> <NP>}       #To extract Prepositional Phrases
#                     VP: {<V> <NP|PP>*}   #To extract Verb Phrases
#                     """)
# output = chunker.parse(tagged)
# print("Output = \n", output)
# output.draw()
#
# tagged = nltk.pos_tag(tokens)
# print(tagged)

# t = treebank.parsed_sents('wsj_0001.mrg')[0]
# t.draw()

# from Parser import Parser
#
#
#
# parser = Parser(model_path=r"C:\Users\tony_\Downloads\stanford-corenlp-4.2.0-models-english\edu\stanford\nlp\models\lexparser\englishPCFG.caseless.ser.gz",
#                 path_to_jar=r"C:\Users\tony_\Downloads\stanford-parser-4.2.0\stanford-parser-full-2020-11-17\stanford-parser.jar",
#                 path_to_models_jar=r"C:\Users\tony_\Downloads\stanford-parser-4.2.0\stanford-parser-full-2020-11-17\stanford-parser-4.2.0-models.jar")
#
# result=parser.parse_sentence("They are eating an apple and an orange and he is sleeping")
# #result=parser.parse_sentence("They are drinking and they are singing")
# print(result)
# #parser.tree_draw()
# parser.tree_sentence()