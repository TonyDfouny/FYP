def TranslateOnline(sourcesentence):
    """

    :param sourcesentence: 'sentence in english'
    :return: 'sentence in arabic'
    """
    import translators as ts
    translatedsentence=ts.translate_text(sourcesentence,'google','en','ar')
    return translatedsentence


def TranslateOffline(sourcesentence):
    """

    :param sourcesentence: 'sentence in english'
    :return: 'sentence in arabic'
    """

    import argostranslate.translate
    from_code = "en"
    to_code = "ar"
    translatedsentence = argostranslate.translate.translate(sourcesentence, from_code, to_code)

    return translatedsentence

"""
آكل false translation lezim tkoun أأكل
"""
#####TESTTT#######
#####ONLINE#######

#import translators as ts
# import translators as ts
# for i in ts.translators_pool:
#         print(i)
# help(ts.translate_text)
# print(ts.translators_pool)
#
# sourcesentence= " Hello my name is Tony "
# translatedsentence=ts.translate_text(sourcesentence,'google','en','ar')
#
# print(translatedsentence)

#print(ts.translate_text(input,'google','en','ar'))

######OFFLINE########
#import argostranslate.translate
#
# from_code = "en"
# to_code = "ar"
#
#
# # Translate
# translatedText = argostranslate.translate.translate("the girls and the woman are playing", from_code, to_code)
#
# print(translatedText)