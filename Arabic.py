from Parser import Parser
# from ar_corrector.corrector import Corrector
from tashaphyne.stemming import ArabicLightStemmer
# corr = Corrector()

# source_sentence="نَحْنُ أَكَلْنَا أسد"
# # #source_sentence="نَحْنُ "
# parser = Parser(model_path=r"C:\Users\tony_\Downloads\stanford-corenlp-4.2.0-models-arabic\edu\stanford\nlp\models\lexparser\arabicFactored.ser.gz",
#                 path_to_jar=r"C:\Users\tony_\Downloads\stanford-parser-4.2.0\stanford-parser-full-2020-11-17\stanford-parser.jar",
#                 path_to_models_jar=r"C:\Users\tony_\Downloads\stanford-parser-4.2.0\stanford-parser-full-2020-11-17\stanford-parser-4.2.0-models.jar")

# #parser mac
# # parser = Parser(model_path=r"/Users/TonyDfouny/Downloads/corenlp/edu/stanford/nlp/models/lexparser/arabicFactored.ser.gz",
# #                 path_to_jar=r"/Users/TonyDfouny/Downloads/stanford-parser-full-2020-11-17/stanford-parser.jar",
# #                 path_to_models_jar=r"/Users/TonyDfouny/Downloads/stanford-parser-full-2020-11-17/stanford-parser-4.2.0-models.jar")
#

# def ArabicParser(arabicsentence):
#     parsedsentence=parser.custom_parse(arabicsentence)
#     return parsedsentence
#
# parsedsentence=ArabicParser(source_sentence)
# #parsedsentence=['PRP نحن', 'VBD اكلنا', 'NNP اسد','VBG اكلنا']
# print (parsedsentence)

def TranslateVerb(words):
    verb=words.split()
    if verb[0]=='VBD':
        output=pastverb(verb[1])
    elif verb[0]=='VBG':
        output=presentverb(verb[1])

    return output


db={}
# def TranslateSentence(sourcesentence):
#     parsedsentence=ArabicParser(sourcesentence)
#     output_sentence=[]
#     for words in parsedsentence:
#         if words[0]=='V':
#             #word = words.split()[1]
#             output_sentence.append(TranslateVerb(words))
#         else:
#             word=words.split()[1]
#             output_sentence.append(db[word])



def presentverb(verb):
    # parsedverb = []
    # for verb in parsedsentence:
    #     if 'V' in verb[0]:
    #         parsedverb.append(verb)
    #
    # print(parsedverb)
    from nltk.stem import arlstem2
    stemmer = arlstem2.ARLSTem2()
    grammar=stemmer.presentverb(stemmer.norm(verb))

    presentdict={('ا',):'1p.s.c.',('',''):'1p.s.c.',
                 ('ت',):'2p.s.m.',
                 ('ت', 'ين'):'2p.s.f',
                 ('ي',):'3p.s.m.',
                 ('ت',):'3p.s.f',
                 ('ن',):'1p.pl.c.',
                 ('ت', 'ون'):'2p.pl.m',
                 ('ت', 'ن'):'2p.pl.f.',
                 ('ي', 'ون'):'3p.pl.c',('ي', 'ن'):'3p.pl.c',('ت', 'ان'):'3p.pl.c',('ي', 'ان'):'3p.pl.c'       ###تأكلان NO DUAL IN PHOE, ONLY PLURIAL
    }
    return presentdict[grammar[1:]]


words=['تأكل','تأكلين','يأكل','تأكل','نأكل','تأكلون','تأكلن','يأكلون','يأكلن','تأكلان','يأكلان','تأكلان','ألعب','أأكل']
for word in words:
    print(word)
    #print(stemmer.verb(word))
    print(presentverb(word))
def pastverb(verb):
    pastdict = {('',''):'1p.s.c.',
                 ():'2p.s.m.',
                 ():'2p.s.f',
                 ():'3p.s.m.',
                 ():'3p.s.f',
                 ():'1p.pl.c.',
                 ():'2p.pl.m',
                 ():'2p.pl.f.',
                 ():'3p.pl.c'
                }
    return None


#print(str(parsed[0]))
#parser.custom_print()
# t=parser.custom_print()
# for i in t:
#     print(i)

# Pronouns = [(parent_tag(tag, word)) for parent_tag, word, tag in parsed]
# print('Pronouns = ',Pronouns)


# print(parsedsentence)
# print(parser.custom_parse(source_sentence))

# parser.custom_print()
# parser.tree_draw()

#print(parser.custom_parse(source_sentence))

# def Translator(source_sentence):
#     ####DATABASE####
#     DB = {"أنا": "𐤀𐤍𐤊",
#           "نَحْنُ": "𐤀𐤍𐤇𐤍",
#           "أكلت": "𐤀𐤊𐤋𐤕",
#           "أَكَلْنَا": "𐤀𐤊𐤋𐤍",
#           "أسد": "𐤀𐤓𐤅"
#           }
#
#     ar_to_phoe_dict = {}
#     for i in source_sentence.split():
#         ar_to_phoe_dict[i] = ''
#
#     for i in ar_to_phoe_dict.keys():
#         if i in DB.keys():
#             ar_to_phoe_dict[i] = DB[i]
#
#     ##Target sentence##
#
#     target_sentence = ""
#     for i in ar_to_phoe_dict.values():
#         target_sentence = target_sentence + " " + i
#
#     print(source_sentence, '\n', target_sentence)
#
#
# Translator(source_sentence)




# result=parser.parse_sentence(u'أنا أقوم ببناء منزل')
# print(result)
# parser.tree_print()
# parser.tree_draw()

###########CORRECTORR##############
#
#
# #####CORRECT WORD SPELLING######
# corr.spell_correct('بختب') # return 5 corrections with top frequencies
# # [('بكتب', 61), ('برتب', 22), ('بختم', 21), ('بختي', 9), ('بخت', 7)]
#
# corr.spell_correct('بختب', 2) # return 2 corrections with top frequencies
# # [('بكتب', 61), ('برتب', 22),]
#
# corr.spell_correct('بختب', 1) # return 1 correction with top frequency
# # [('بكتب', 61)]
#
# corr.spell_correct('لتمشتلميتلكب', 4) # return the same word
# # لتمشتلميتلكب
#
# corr.spell_correct('من') # return true
# # True
#
#
# #####CONTEXT CORRECTION#####
# sent = 'أكدت قواءص التمذد في تشاد أنها تواضضل طريقها للعاحمة'
# print(corr.contextual_correct(sent))
# #أكدت قوات التمرد في تشاد أنها تواصل طريقها للعاصمة
#
# sent = 'اتتنتهى حدث آبل المنتظو بالإعلاخ عن مموعة من المنتجات'
# print(corr.contextual_correct(sent))
# #انتهى حدث آبل المنتظر الإعلان عن مجموعة من المنتجات