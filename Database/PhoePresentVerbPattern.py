class PhoePresentVerbPattern:
    def __init__(self,verb,person):
        self.verb=verb
        self.person=person
        
    def __StrongPattern(self):
        Pattern={
                "1p.s.c.":"ʾ"+self.verb,
                "2p.s.m.":"t"+self.verb,
                "2p.s.f.":"t"+self.verb,
                "3p.s.m.":"y"+self.verb,
                "3p.s.f.":"t"+self.verb,
                "1p.pl.c.":"n"+self.verb,
                "2p.pl.m.":"t"+self.verb+"n",
                "2p.pl.f.":"t"+self.verb+"n",
                "3p.pl.c.":"y"+self.verb+"n"
                 }
        return Pattern[self.person]

    def __WeakPattern_1y__ytn(self):

        Pattern = {
            "1p.s.c.": "ʾ" + self.verb[1]+self.verb[2],
            "2p.s.m.": "t" + self.verb[1]+self.verb[2],
            "2p.s.f.": "t" + self.verb[1]+self.verb[2],
            "3p.s.m.": "y" + self.verb[1]+self.verb[2],
            "3p.s.f.": "t" + self.verb[1]+self.verb[2],
            "1p.pl.c.": "n" + self.verb[1]+self.verb[2],
            "2p.pl.m.": "t" + self.verb[1]+self.verb[2]+ "n",
            "2p.pl.f.": "t" + self.verb[1]+self.verb[2] + "n",
            "3p.pl.c.": "y" + self.verb[1]+self.verb[2] + "n"
        }
        return Pattern[self.person]

    def __WeakPattern_2y__2w(self):
        """
        :return:'self.verb with the correct grammar'
        """
        Pattern = {
            "1p.s.c.": "ʾ" + self.verb[0] + self.verb[2],
            "2p.s.m.": "t" + self.verb[0] + self.verb[2],
            "2p.s.f.": "t" + self.verb[0] + self.verb[2],
            "3p.s.m.": "y" + self.verb[0] + self.verb[2],
            "3p.s.f.": "t" + self.verb[0] + self.verb[2],
            "1p.pl.c.": "n" + self.verb[0] + self.verb[2],
            "2p.pl.m.": "t" + self.verb[0] + self.verb[2] + "n",
            "2p.pl.f.": "t" + self.verb[0] + self.verb[2] + "n",
            "3p.pl.c.": "y" + self.verb[0] + self.verb[2] + "n"
        }
        return Pattern[self.person]

    def __WeakPattern_3y(self):
        """
        :return:'self.verb with the correct grammar'
        """
        Pattern = {
            "1p.s.c.": "ʾ" + self.verb[0] + self.verb[1],
            "2p.s.m.": "t" + self.verb[0] + self.verb[1],
            "2p.s.f.": "t" + self.verb[0] + self.verb[1],
            "3p.s.m.": "y" + self.verb[0] + self.verb[1],
            "3p.s.f.": "t" + self.verb[0] + self.verb[1],
            "1p.pl.c.": "n" + self.verb[0] + self.verb[1],
            "2p.pl.m.": "t" + self.verb[0] + self.verb[1] + "n",
            "2p.pl.f.": "t" + self.verb[0] + self.verb[1] + "n",
            "3p.pl.c.": "y" + self.verb[0] + self.verb[1] + "n"
        }
        return Pattern[self.person]


    def PresentPattern(self):
        """
        :return:
        """
        if self.verb[0]=='y': ###########YTN?????????#################
            return self.__WeakPattern_1y__ytn()
        elif self.verb[1]=='y' or self.verb[1]=='w':
            return self.__WeakPattern_2y__2w()
        elif self.verb[2]=='y':
            return self.__WeakPattern_3y()
        else:
            return self.__StrongPattern()

