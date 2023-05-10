class PhoePastVerbPattern:
    def __init__(self,verb,person):
        """
        :param verb: root verb in phoe
        :param person: person
        """
        self.verb=verb
        self.person=person

    def __StrongPattern(self):
        """
        :return:'verb with the correct grammar'
        """
        Pattern = {
            "1p.s.c.": self.verb + "t",
            "2p.s.m.": self.verb + "t",
            "2p.s.f.": self.verb + "t",
            "3p.s.m.": self.verb,
            "3p.s.f.": self.verb,
            "1p.pl.c.": self.verb + "n",
            "2p.pl.m.": self.verb + "tm",
            "2p.pl.f.": self.verb + "tn",
            "3p.pl.c.": self.verb
        }
        return Pattern[self.person]

    def __StrongPattern_3n(self):
        """
        :return:'verb with the correct grammar'
        """
        Pattern = {
            "1p.s.c.": self.verb[0] + self.verb[1] + "t",
            "2p.s.m.": self.verb[0] + self.verb[1] + "t",
            "2p.s.f.": self.verb[0] + self.verb[1] + "t",
            "3p.s.m.": self.verb,
            "3p.s.f.": self.verb,
            "1p.pl.c.": self.verb,
            "2p.pl.m.": self.verb[0] + self.verb[1] + "tm",
            "2p.pl.f.": self.verb[0] + self.verb[1] + "tn",
            "3p.pl.c.": self.verb
        }
        return Pattern[self.person]

    def __WeakPattern_3y__3w(self):
        """

        :param self.verb: 'self.verb' root self.verb in phoenician
        :param person: 'person'
        :return:'self.verb with the correct grammar'
        """
        Pattern = {
            "1p.s.c.": self.verb[0] + self.verb[1] + "t",
            "2p.s.m.": self.verb[0] + self.verb[1] + "t",
            "2p.s.f.": self.verb[0] + self.verb[1] + "t",
            "3p.s.m.": self.verb[0] + self.verb[1],
            "3p.s.f.": self.verb[0] + self.verb[1],
            "1p.pl.c.": self.verb[0] + self.verb[1] + "n",
            "2p.pl.m.": self.verb[0] + self.verb[1] + "tm",
            "2p.pl.f.": self.verb[0] + self.verb[1] + "tn",
            "3p.pl.c.": self.verb[0] + self.verb[1]
        }
        return Pattern[self.person]

    def __WeakPattern_2y__2w__2y_n(self):
        """

        :param self.verb: 'self.verb' root self.verb in phoenician
        :param person: 'person'
        :return:'self.verb with the correct grammar'
        """
        Pattern = {
            "1p.s.c.": self.verb[0] + self.verb[2] + "t",
            "2p.s.m.": self.verb[0] + self.verb[2] + "t",
            "2p.s.f.": self.verb[0] + self.verb[2] + "t",
            "3p.s.m.": self.verb[0] + self.verb[2],
            "3p.s.f.": self.verb[0] + self.verb[2],
            "1p.pl.c.": self.verb[0] + self.verb[2] + "n",
            "2p.pl.m.": self.verb[0] + self.verb[2] + "tm",
            "2p.pl.f.": self.verb[0] + self.verb[2] + "tn",
            "3p.pl.c.": self.verb[0] + self.verb[2]
        }
        return Pattern[self.person]

    def __WeakPattern_2w_n(self):
        """

        :param self.verb: 'self.verb' root self.verb in phoenician
        :param person: 'person'
        :return:'self.verb with the correct grammar'
        """
        Pattern = {
            "1p.s.c.": self.verb[0] + "t",
            "2p.s.m.": self.verb[0] + +"t",
            "2p.s.f.": self.verb[0] + "t",
            "3p.s.m.": self.verb[0] + self.verb[2],
            "3p.s.f.": self.verb[0] + self.verb[2],
            "1p.pl.c.": self.verb[0] + "n",
            "2p.pl.m.": self.verb[0] + "tm",
            "2p.pl.f.": self.verb[0] + "tn",
            "3p.pl.c.": self.verb[0] + self.verb[2]
        }
        return Pattern[self.person]

    def PastPattern(self):
        """
        :return:

        """
        if self.verb[2] == 'n':
            return self.__StrongPattern_3n()
        elif self.verb[2] == 'y' or self.verb[2] == 'w':
            return self.__WeakPattern_3y__3w()
        elif self.verb[1] == 'w' or self.verb[1] == 'y' or (self.verb[1] == 'y' and self.verb[3] == 'n'):
            return self.__WeakPattern_2y__2w__2y_n()
        elif self.verb[1] == 'w' and self.verb[3] == 'n':
            return self.__WeakPattern_2w_n()
        else:
            return self.__StrongPattern()

