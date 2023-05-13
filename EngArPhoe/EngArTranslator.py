class Translator():
    def __init__(self,sourcesentence,from_code,to_code,translationtype):
        """
        :param sourcesentence: 'sentence in source lang'
        :param from_code: 'lang code' en for english
        :param from_code: 'lang code' ar for arabic
        :param translationtype: 'offline or online'
        """
        self.sourcesentence=sourcesentence
        self.from_code=from_code
        self.to_code=to_code
        self.translationtype=translationtype

    def __TranslateOnline(self):
        """
        :return: 'sentence in destination lang'
        """
        import translators as ts
        return ts.translate_text(self.sourcesentence,'google',self.from_code,self.to_code)


    def __TranslateOffline(self):
        """
        :return: 'sentence in destination lang'
        """

        import argostranslate.translate
        # from_code = "en"
        # to_code = "ar"
        return argostranslate.translate.translate(self.sourcesentence,self.from_code,self.to_code)

    def Translate(self):
        """
        :return: 'sentence in destination language'
        """
        if self.translationtype=='Offline':
            return self.__TranslateOffline()
        elif self.translationtype=='Online':
            return self.__TranslateOnline()

    # def ReTranslate(self):
    #     """
    #     :return: 'sentence in english'
    #     """
    #     if self.translationtype=='Offline':
    #         return
    #     elif self.translationtype=='Online':
    #         return

# print(Translator('son','en','ar','Online').Translate())
# print(Translator('son','en','ar','Offline').Translate())
# print(Translator('ابن','ar','en','Online').Translate())
# print(Translator('إبني','ar','en','Online').Translate())