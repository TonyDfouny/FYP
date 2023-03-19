import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
    "I am"
 )
about_doc = nlp(about_text)
for token in about_doc:
     print(
         f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}""" )