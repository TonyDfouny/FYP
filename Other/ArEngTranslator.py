def TranslateOnline(sourcesentence):
    """

    :param sourcesentence: 'sentence in arabic'
    :return: 'sentence in english'
    """
    import translators as ts
    translatedsentence=ts.translate_text(sourcesentence,'google','ar','en')
    for i in ts.translators_pool:
        translatedsentence=ts.translate_text(sourcesentence,i,'ar','en')
        print(i,' ',translatedsentence)
    return translatedsentence


def TranslateOffline(sourcesentence):
    """

    :param sourcesentence: 'sentence in arabic'
    :return: 'sentence in english'
    """

    import argostranslate.translate
    from_code = "ar"
    to_code = "en"
    translatedsentence = argostranslate.translate.translate(sourcesentence, from_code, to_code)

    return translatedsentence

source='هو يأتي مع ابن الى بيروت'
#print(TranslateOffline(source))
print(TranslateOnline(source))