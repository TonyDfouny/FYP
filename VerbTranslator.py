import Finder

def presentverb(verb):
    """

    :param verb: 'verb'
    :return: ['rootverb','person']
    """
    from nltk.stem import arlstem2
    stemmer = arlstem2.CustomARLSTem2()
    grammar=stemmer.presentverb(stemmer.norm(verb)) #Present verb custom fct in arlstem2.py (not pushed in github)
    #print(grammar) ('اكل', 'ت', 'ين')
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

    output=[grammar[0],presentdict[grammar[1:]]]

    return output

def pastverb(verb):
    """

    :param verb: 'verb'
    :return: ['rootverb','person']
    """
    from tashaphyne.stemming import ArabicLightStemmer
    ArListem = ArabicLightStemmer()
    ArListem.light_stem(verb)
    suffix=ArListem.get_suffix()
    l = len(suffix)
    rootverb = verb[:-l]
    pastdict = {('ت'):'1p.s.c.',
                 ('ت'):'2p.s.m.',
                 ('ت'):'2p.s.f',
                 (''):'3p.s.m.',
                 ('ت'):'3p.s.f',
                 ('نا'):'1p.pl.c.',
                 ('تم'):'2p.pl.m',
                 ('تن'):'2p.pl.f.',
                 ('وا'):'3p.pl.c',('ن'):'3p.pl.c',('تما'):'3p.pl.c',('ا'):'3p.pl.c'
                }

    output=[rootverb,pastdict[suffix]]
    return output

# def FindVerb(rootverb,person):
#     """
#
#     :param rootverb: 'rootverb'
#     :param person:  'person'
#     :return: 'verb in phoe'
#     """
#     #get translated verb where dict[rootverb] and person[person]
#     infphoeverb=DB.ArPhoeDB[rootverb]
#     phoeverb=DB.VerbDB[infphoeverb][person]
#     #print('root =',rootverb,'\n',person)
#
#     return phoeverb

#FindVerb(pastverb(words[0])[0],pastverb(words[0])[1])

def VerbTranslator(words):
    """

    :param words: 'verb TAG'
    :return:  'verb in phoe'
    """
    verb=words.split()
    pastTags=['VB','VBD','VBN']
    presentTags=['VBG','VBP','VBZ']
    try:
        if verb[0] in pastTags:
            details=pastverb(verb[1])
            rootverb=details[0]
            person=details[1]
            output=Finder.FindVerb(rootverb,person)
        elif verb[0] in presentTags:
            details = presentverb(verb[1])
            rootverb = details[0]
            person = details[1]
            output=Finder.FindVerb(rootverb,person)

        return output
    except KeyError:
        return Finder.FindWord(verb[1])

########TEST###########
#print(VerbTranslator('VBP ياتي'))

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

