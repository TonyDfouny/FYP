import Finder
import PhoePastVerbPattern
import PhoePresentVerbPattern

class VerbTranslator:
    def __init__(self,verbs,translationtype):
        """
        :param words: 'verb TAG'
        :param translationtype: 'online or offline'
        """
        self.verbs=verbs
        self.translationtype=translationtype
        self.TAG = self.verbs.split()[0]
        self.verb=self.verbs.split()[1]

    def __presentverb(self):
        """
        :return: ['rootverb','person']
        """
        from nltk.stem import arlstem2
        stemmer = arlstem2.CustomARLSTem2()
        grammar=stemmer.presentverb(stemmer.norm(self.verb)) #Present verb custom fct in arlstem2.py (not pushed in github)
        #print(grammar) ('اكل', 'ت', 'ين')
        presentdict={('ا',):'1p.s.c.',('',''):'1p.s.c.',
                     ('ت',):'2p.s.m.',
                     ('ت', 'ين'):'2p.s.f.',
                     ('ي',):'3p.s.m.',
                     ('ت',):'3p.s.f.',
                     ('ن',):'1p.pl.c.',
                     ('ت', 'ون'):'2p.pl.m.',
                     ('ت', 'ن'):'2p.pl.f.',
                     ('ي', 'ون'):'3p.pl.c.',('ي', 'ن'):'3p.pl.c.',('ت', 'ان'):'3p.pl.c.',('ي', 'ان'):'3p.pl.c.'       ###تأكلان NO DUAL IN PHOE, ONLY PLURIAL
        }

        try:
            return [grammar[0],presentdict[grammar[1:]]]
        except KeyError:
            if type(grammar)==tuple:
                return [grammar[0],'2p.s.m.']
            else:
                return [self.verb,'2p.s.m.']
        except TypeError:
            if type(grammar)==tuple:
                return [grammar[0],'2p.s.m.']
            else:
                return [self.verb,'2p.s.m.']

    def __pastverb(self):
        """
        :return: ['rootverb','person']
        """
        from tashaphyne.stemming import ArabicLightStemmer
        ArListem = ArabicLightStemmer()
        ArListem.light_stem(self.verb)
        suffix=ArListem.get_suffix()
        l = len(suffix)
        if l==0:
            rootverb=self.verb
        else:
            rootverb = self.verb[:-l]

        pastdict = {('ت'):'1p.s.c.',
                     ('ت'):'2p.s.m.',
                     ('ت'):'2p.s.f.',
                     (''):'3p.s.m.',
                     ('ت'):'3p.s.f.',
                     ('نا'):'1p.pl.c.',
                     ('تم'):'2p.pl.m.',
                     ('تن'):'2p.pl.f.',
                     ('وا'):'3p.pl.c.',('ن'):'3p.pl.c.',('تما'):'3p.pl.c.',('ا'):'3p.pl.c.'
                    }

        try:
            return [rootverb,pastdict[suffix]]
        except KeyError:
            return [rootverb,'2p.s.m.']
        except TypeError:
            return [rootverb, '2p.s.m.']


    def Translate(self):
        """
        :return:  'verb in phoe'
        """
        pastTags=['VB','VBD','VBN']
        presentTags=['VBG','VBP','VBZ']
        if self.TAG in pastTags:
            details=self.__pastverb()
            rootverb=details[0]
            person=details[1]

            phoerootverb=Finder.FindVerb(self.verb,rootverb,self.translationtype)
            print('root ', rootverb, ' original ', self.verb, ' phoeroot ', phoerootverb, ' person ', person)
            if phoerootverb==self.verb:
                return self.verb
            else:
                return PhoePastVerbPattern.PhoePastVerbPattern(phoerootverb,person).PastPattern()

        elif self.TAG in presentTags:
            details = self.__presentverb()
            rootverb = details[0]
            person = details[1]

            phoerootverb=Finder.FindVerb(self.verb,rootverb,self.translationtype)
            print('root ', rootverb, ' original ', self.verb,' phoeroot ',phoerootverb,' person ',person)
            if phoerootverb==self.verb:
                return self.verb
            else:
                return PhoePresentVerbPattern.PhoePresentVerbPattern(phoerootverb,person).PresentPattern()





#print(VerbTranslator('VBD أجمع','Offline'))
########TEST###########
#print(VerbTranslator('VBP تجد','Offline').Translate())

# words=['تأكل','تأكلين']#,'يأكل','تأكل','نأكل','تأكلون','تأكلن','يأكلون','يأكلن','تأكلان','يأكلان','تأكلان','ألعب','أأكل']
# for word in words:
#     print(word)
#     #print(stemmer.verb(word))
#     print(presentverb(word))

#words=['اكلت','اكلت'] #,'اكلت','اكل','اكلت','اكلنا','اكلتم','اكلتن','اكلوا','اكلن','اكلتما','اكلا','اكلتا']
# for word in words:
#     print(word)
#     #print(stemmer.verb(word))
#     print(pastverb(word))

