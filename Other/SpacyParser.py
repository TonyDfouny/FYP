import spacy
nlp = spacy.load("en_core_web_sm")
sentence ="They are eating an apple and an orange.Tony is sleeping"
sentence2="Tony Dfouny,the kids and I are sleeping"
sentence3='There are many factors affecting teacher retention'
doc = nlp(sentence2)
doc2=nlp(sentence3)



# for token in doc2:
#     print(token.text, "\t", token.dep_, "\t",
#     spacy.explain(token.dep_))
#     ancestors = [t.text for t in token.ancestors]
#     print(ancestors)

# for token in doc:
#     print(
#         f"""
#     TOKEN: {str(token)}
#     =====
#     TAG: {str(token.tag_):10} POS: {token.pos_}
#     EXPLANATION: {spacy.explain(token.tag_)}""")
#     if token.dep_=='nsubj':
#         ancestors = [t.text for t in token.ancestors]
#         print(token.text,'verb = ',ancestors)



# for token in doc:
#     print(token.text)
#     for t in token.children:
#         if t.dep_=='nsubj':
#             children=[t.text]
#             print(children)











##############ORIGINAL###################

#########TAGS#########
for token in doc:
     print(
         f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}""" )

##########DEPENDENCY#########
for token in doc:
    print(token.text, "\t", token.dep_, "\t",
    spacy.explain(token.dep_))

########ANCESTORS###########
# for token in doc:
#     print(token.text)
#     ancestors = [t.text for t in token.ancestors]
#     print(ancestors)


########CHILDREN##########
# for token in doc:
#     print(token.text)
#     children = [t.text for t in token.children]
#     print(children)