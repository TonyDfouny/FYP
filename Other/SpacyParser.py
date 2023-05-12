import spacy
nlp = spacy.load("en_core_web_sm")
sentence ="eat"
sentence2="I am sleeping, he made it for Byblos"
sentence3='There are many factors affecting teacher retention'
doc = nlp(sentence2)
doc2=nlp(sentence3)



# for token in doc:
#     #print(token.text, "\t", token.dep_, "\t")
#     #print(spacy.explain(token.dep_))
#     print(token)
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

parsedsentence=[]
allchildren={}
for token in doc:
    parsedsentence.append([str(token), str(token.tag_), str(token.dep_)])
    allchildren[str(token)] = []
    # allchildren[str(token)].append('hi')
    for child in token.children:
        if str(token) in allchildren.keys():
            allchildren[str(token)].append(([str(child.text), str(child.tag_), str(child.dep_)]))
        else:
            allchildren[str(token)] = [str(child.text), str(child.tag_), str(child.dep_)]
print('parsed ',parsedsentence)
print('allchildren',allchildren)

# for token in doc:
#     print(token.text, token.tag_ , token.dep_)
#     if token.tag_[0]=='V':
#         for child in token.children:
#             children=[child.text,child.tag_,child.dep_]
#             print(children)
    # for t in token.children:
    #     children = [t.text, t.tag_, t.dep_]
    #     print(children)
    #     # if t.dep_=='nsubj' or t.dep_=='aux':
    #     #     children=[t.text,t.tag_,t.dep_]
    #     #     print(children)

# for token in doc:
#     print([token,token.tag_])
    #print('TOKEN: '[str(token),'TAG: ',str(token.tag_)])








##############ORIGINAL###################

#########TAGS#########
# for token in doc:
#      print(
#          f"""
# TOKEN: {str(token)}
# =====
# TAG: {str(token.tag_):10} POS: {token.pos_}
# EXPLANATION: {spacy.explain(token.tag_)}""" )
#
# ##########DEPENDENCY#########
# for token in doc:
#     print(token.text, "\t", token.dep_, "\t",
#     spacy.explain(token.dep_))

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