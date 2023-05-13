import PhoeWordFinder

class PhoePossessiveFinder:
    def __init__(self,word):
        self.word=word

    def __Possessive(self):
        poss = {
            'y': 'my',
            'k': 'your','km':'your',
            'h': 'his',
            'n': 'our',
            'm': 'their'
        }
        try:
            engword = PhoeWordFinder.PhoeWordFinder(self.word[:-2]).WordFinder()
        except KeyError:
            engword =self.word
        if engword != self.word:
            try:
                return poss[self.word[-2:]] + ' ' + engword
            except KeyError:
                pass

        try:
            engword = PhoeWordFinder.PhoeWordFinder(self.word[:-1]).WordFinder()
        except KeyError:
            engword = self.word
        if engword != self.word:
            try:
                return poss[self.word[-1]] + ' ' + engword
            except KeyError:
                return None
        else:
            return None



    # def __CheckTranslate(self):
    #     if

    # def Translate(self):
    #     if self.__CheckTranslate() is None:
    #         raise KeyError
    #     else:
    #         return self.__CheckTranslate()

    def Translate(self):
        possesive = self.__Possessive()
        if possesive is None:
            raise KeyError
        else:
            return possesive


#print(PhoePossessiveFinder('šmš').Translate())