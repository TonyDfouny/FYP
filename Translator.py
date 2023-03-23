#####ONLINE#######
#import translators as ts

# help(ts.translate_text)
# print(ts.translators_pool)

sourcesentence= " Hello my name is Tony "


#print(ts.translate_text(input,'google','en','ar'))

######OFFLINE########
import argostranslate.translate
#
# from_code = "en"
# to_code = "ar"
#
#
# # Translate
# translatedText = argostranslate.translate.translate("the girls and the woman are playing", from_code, to_code)
#
# print(translatedText)

def TranslateOnline(sourcesentence):
    import translators as ts
    translatedsentence=ts.translate_text(input,'google','en','ar')
    return translatedsentence


def TranslateOffline(sourcesentence):

    from_code = "en"
    to_code = "ar"
    translatedsentence = argostranslate.translate.translate(sourcesentence, from_code, to_code)

    return translatedsentence
