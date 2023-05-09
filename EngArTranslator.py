def TranslateOnline(sourcesentence,from_code,to_code):
    """
    :param sourcesentence: 'sentence in source lang'
    :param from_code: 'lang code' en for english
    :param from_code: 'lang code' ar for arabic
    :return: 'sentence in destination lang'
    """
    import translators as ts
    translatedsentence=ts.translate_text(sourcesentence,'google',from_code,to_code)
    return translatedsentence


def TranslateOffline(sourcesentence,from_code,to_code):
    """
    :param sourcesentence: 'sentence in source lang'
    :param from_code: 'lang code' en for english
    :param from_code: 'lang code' ar for arabic
    :return: 'sentence in destination lang'
    """

    import argostranslate.translate
    # from_code = "en"
    # to_code = "ar"
    translatedsentence = argostranslate.translate.translate(sourcesentence, from_code, to_code)

    return translatedsentence

def Translate(sourcesentence,translationtype):
    """

    :param sourcesentence: 'sentence in english'
    :param translationtype: 'offline or online'
    :return: 'sentence in arabic'
    """
    if translationtype=='Offline':
        return TranslateOffline(sourcesentence,'en','ar')
    elif translationtype=='Online':
        return TranslateOnline(sourcesentence,'en','ar')

def ReTranslate(sourcesentence,translationtype):
    """

    :param sourcesentence: 'sentence in arabic'
    :param translationtype: 'offline or online'
    :return: 'sentence in english'
    """
    if translationtype=='Offline':
        return TranslateOffline(sourcesentence,'ar','en')
    elif translationtype=='Online':
        return TranslateOnline(sourcesentence,'ar','en')




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