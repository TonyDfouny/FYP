import json
import PhoePresentVerbPattern
import PhoePastVerbPattern
class EngPhoeVerbTranslator:
    def __init__(self,verb,allchildren):
        """

        :param verb: verb in english with tag
        """
        from snowballstemmer import stemmer
        en_stemmer = stemmer("english")
        self.verb=verb[0]
        self.tag=verb[1]
        self.rootverb=en_stemmer.stemWord(str(self.verb))
        self.children=allchildren
    def __verbfinder(self):
        """

        :return: rootverb in phoenician
        """
        verbs = open('VERBDATABASE.json', 'r', encoding='utf-8')
        verbsDB = json.load(verbs)

        for line in verbsDB:
            if self.rootverb in line['English'].split(','):
                if line['root_t']!='':
                    return line['root_t']


    def __VerbFinder(self):


        if self.__verbfinder() is None:
            raise KeyError
        else:
            return self.__verbfinder()


    def __ChildrenAndPast(self):
        andperson = {
            'I': '1p.pl.c.', 'WE': '1p.pl.c.',
            'YOU': '2p.pl.m.',
            'HE': '3p.pl.c.', 'SHE': '3p.pl.c.', 'IT': '3p.pl.c.', 'HIM': '3p.pl.c.', 'HER': '3p.pl.c.',
            'THEY': '3p.pl.c.', 'THEM': '3p.pl.c.'
        }
        person = {
            'I': '1p.s.c.',
            'YOU': '2p.pl.m.',
            'HE': '3p.s.m.', 'SHE': '3p.s.f.', 'IT': '3p.s.m.',
            'WE': '1p.pl.c.',
            'THEY': '3p.pl.c.'
        }
        verbsubject = []
        for child in self.children[self.verb]:
            if child[2] == 'nsubj' :
                verbsubject.append(child[0])
        if len(verbsubject)==0: ####no subject found as pronouns
                return self.__VerbFinder()
        elif len(verbsubject)>1: ####at least one pronoun + another subject in subject
            subject=verbsubject[-1]
            if subject.upper() in andperson.keys():
                return PhoePastVerbPattern.PhoePastVerbPattern(self.__VerbFinder(),person[subject.upper()]).PastPattern()
            else:
                return self.__VerbFinder()
        elif len(verbsubject)==1: ####exactly one subject and it is a pronoun
            if verbsubject[0].upper() in person.keys():
                return PhoePastVerbPattern.PhoePastVerbPattern(self.__VerbFinder(),person[verbsubject[0].upper()]).PastPattern()
            else:
                return self.__VerbFinder()


    def __ChildrenAndPresent(self):
        andperson={
            'I':'1p.pl.c.','WE':'1p.pl.c.',
            'YOU':'2p.pl.m.',
            'HE':'3p.pl.c.','SHE':'3p.pl.c.','IT':'3p.pl.c.','HIM':'3p.pl.c.','HER':'3p.pl.c.','THEY':'3p.pl.c.','THEM':'3p.pl.c.'
        }
        person = {
            'I': '1p.s.c.',
            'YOU': '2p.pl.m.',
            'HE': '3p.s.m.', 'SHE': '3p.s.f.', 'IT': '3p.s.m.',
            'WE': '1p.pl.c.',
            'THEY': '3p.pl.c.'
        }
        aux={
            'AM': '1p.s.c.',
            'IS': '3p.s.m.',
            'ARE': '2p.pl.m.'
        }
        verbaux=[]
        verbsubject=[]

        for child in self.children[self.verb]:
            if child[2]=='aux':
                verbaux.append(child[0])
            elif child[2]=='nsubj':
                verbsubject.append(child[0])
        if len(verbsubject)==0 and len(verbaux) == 0: ####no subject found as pronouns and no aux###
                return self.__VerbFinder()


        elif len(verbsubject)>1: ####at least one pronoun + another subject in subject
            subject=verbsubject[-1]

            if subject.upper() in andperson.keys():
                return PhoePresentVerbPattern.PhoePresentVerbPattern(self.__VerbFinder(),person[subject.upper()]).PresentPattern()
            elif len(verbaux) > 0:  ###no pronouns was found in subject but at least the aux
                if verbaux[0].upper() in aux.keys():
                    return PhoePresentVerbPattern.PhoePresentVerbPattern(self.__VerbFinder(),
                                                                         aux[verbaux[0].upper()]).PresentPattern()
                else:
                    return self.__VerbFinder()

        elif len(verbsubject)==1: ####exactly one subject and it is a pronoun

            if verbsubject[0].upper() in person.keys():
                return PhoePresentVerbPattern.PhoePresentVerbPattern(self.__VerbFinder(),person[verbsubject[0].upper()]).PresentPattern()
            elif len(verbaux) > 0:  ###no pronouns was found in subject but at least the aux
                if verbaux[0].upper() in aux.keys():
                    return PhoePresentVerbPattern.PhoePresentVerbPattern(self.__VerbFinder(),
                                                                         aux[verbaux[0].upper()]).PresentPattern()
                else:
                    return self.__VerbFinder()


        elif len(verbaux)>0:###no pronouns was found in subject but at least the aux
            if verbaux[0].upper() in aux.keys():
                return PhoePresentVerbPattern.PhoePresentVerbPattern(self.__VerbFinder(),aux[verbaux[0].upper()]).PresentPattern()
            else:
                return self.__VerbFinder()





    def __CheckTranslate(self):
        pastTags = ['VB', 'VBD', 'VBN']
        presentTags = ['VBG', 'VBP', 'VBZ']

        try:
            self.children[self.verb]
        except KeyError:
            return self.__VerbFinder()
        if self.tag in pastTags:
            return self.__ChildrenAndPast()
        elif self.tag in presentTags:
            return self.__ChildrenAndPresent()

    def Translate(self):
        if self.__CheckTranslate() is None:
            raise KeyError
        else:
            return self.__CheckTranslate()



# import spacy
# nlp = spacy.load("en_core_web_sm")
# sentence ="eat"
# sentence2="I am sleeping, we ate the food"
# sentence3='There are many factors affecting teacher retention'
# doc = nlp(sentence2)
#
#
# parsedsentence = []
# allchildren={}
# for token in doc:
#     parsedsentence.append([str(token), str(token.tag_),str(token.dep_)])
#     allchildren[str(token)] = []
#     # allchildren[str(token)].append('hi')
#     for child in token.children:
#         if str(token) in allchildren.keys():
#             allchildren[str(token)].append(([str(child.text), str(child.tag_), str(child.dep_)]))
#         else:
#             allchildren[str(token)] = [str(child.text), str(child.tag_), str(child.dep_)]
#
# print(parsedsentence)
# print(EngPhoeVerbTranslator(parsedsentence[5],allchildren).Translate())