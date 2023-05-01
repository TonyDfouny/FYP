def ArabicParser(arabicsentence):
    """

    :param arabicsentence: 'source sentence in arabic'
    :return: ['word TAG','word TAG',...]
    """
    from Parser import Parser


    parser = Parser(
        model_path=r"C:\Users\tony_\Downloads\stanford-corenlp-4.2.0-models-arabic\edu\stanford\nlp\models\lexparser\arabicFactored.ser.gz",
        path_to_jar=r"C:\Users\tony_\Downloads\stanford-parser-4.2.0\stanford-parser-full-2020-11-17\stanford-parser.jar",
        path_to_models_jar=r"C:\Users\tony_\Downloads\stanford-parser-4.2.0\stanford-parser-full-2020-11-17\stanford-parser-4.2.0-models.jar")

    # #parser mac
    # # parser = Parser(model_path=r"/Users/TonyDfouny/Downloads/corenlp/edu/stanford/nlp/models/lexparser/arabicFactored.ser.gz",
    # #                 path_to_jar=r"/Users/TonyDfouny/Downloads/stanford-parser-full-2020-11-17/stanford-parser.jar",
    # #                 path_to_models_jar=r"/Users/TonyDfouny/Downloads/stanford-parser-full-2020-11-17/stanford-parser-4.2.0-models.jar")
    #

    parsedsentence=parser.custom_parse(arabicsentence)
    return parsedsentence



########TEST###########
print(ArabicParser('الحيوانات'))
print(ArabicParser('الحيوان'))








"""





source_sentence = "نَحْنُ أَكَلْنَا أسد"
    # #source_sentence="نَحْنُ "


parsedsentence=ArabicParser(source_sentence)
#parsedsentence=['PRP نحن', 'VBD اكلنا', 'NNP اسد','VBG اكلنا']
print(parsedsentence)




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

"""