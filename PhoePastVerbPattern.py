def StrongPattern(verb,person):
    """

    :param verb: 'verb' root verb in phoenician
    :param person: 'person'
    :return:'verb with the correct grammar'
    """
    Pattern={
            "1p.s.c.":verb+"t",
            "2p.s.m.":verb+"t",
            "2p.s.f.":verb+"t",
            "3p.s.m.":verb,
            "3p.s.f.":verb,
            "1p.pl.c.":verb+"n",
            "2p.pl.m.":verb+"tm",
            "2p.pl.f.":verb+"tn",
            "3p.pl.c.":verb
             }
    return Pattern[person]

def StrongPattern_3n(verb,person):
    """

    :param verb: 'verb' root verb in phoenician
    :param person: 'person'
    :return:'verb with the correct grammar'
    """
    Pattern = {
        "1p.s.c.": verb[0]+verb[1]+"t",
        "2p.s.m.": verb[0]+verb[1]+"t",
        "2p.s.f.": verb[0]+verb[1]+"t",
        "3p.s.m.": verb,
        "3p.s.f.": verb,
        "1p.pl.c.": verb,
        "2p.pl.m.": verb[0]+verb[1]+"tm",
        "2p.pl.f.": verb[0]+verb[1]+"tn",
        "3p.pl.c.": verb
    }
    return Pattern[person]

def WeakPattern_3y__3w(verb,person):
    """

    :param verb: 'verb' root verb in phoenician
    :param person: 'person'
    :return:'verb with the correct grammar'
    """
    Pattern = {
        "1p.s.c.": verb[0]+verb[1]+"t",
        "2p.s.m.": verb[0]+verb[1]+"t",
        "2p.s.f.": verb[0]+verb[1]+"t",
        "3p.s.m.": verb[0]+verb[1],
        "3p.s.f.": verb[0]+verb[1],
        "1p.pl.c.": verb[0]+verb[1]+"n",
        "2p.pl.m.": verb[0]+verb[1]+"tm",
        "2p.pl.f.": verb[0]+verb[1]+"tn",
        "3p.pl.c.": verb[0]+verb[1]
    }
    return Pattern[person]

def WeakPattern_2y__2w__2y_n(verb,person):
    """

    :param verb: 'verb' root verb in phoenician
    :param person: 'person'
    :return:'verb with the correct grammar'
    """
    Pattern = {
        "1p.s.c.": verb[0]+verb[2]+"t",
        "2p.s.m.": verb[0]+verb[2]+"t",
        "2p.s.f.": verb[0]+verb[2]+"t",
        "3p.s.m.": verb[0]+verb[2],
        "3p.s.f.": verb[0]+verb[2],
        "1p.pl.c.": verb[0]+verb[2]+"n",
        "2p.pl.m.": verb[0]+verb[2]+"tm",
        "2p.pl.f.": verb[0]+verb[2]+"tn",
        "3p.pl.c.": verb[0]+verb[2]
    }
    return Pattern[person]

def WeakPattern_2w_n(verb,person):
    """

    :param verb: 'verb' root verb in phoenician
    :param person: 'person'
    :return:'verb with the correct grammar'
    """
    Pattern = {
        "1p.s.c.": verb[0]+"t",
        "2p.s.m.": verb[0]++"t",
        "2p.s.f.": verb[0]+"t",
        "3p.s.m.": verb[0]+verb[2],
        "3p.s.f.": verb[0]+verb[2],
        "1p.pl.c.": verb[0]+"n",
        "2p.pl.m.": verb[0]+"tm",
        "2p.pl.f.": verb[0]+"tn",
        "3p.pl.c.": verb[0]+verb[2]
    }
    return Pattern[person]


def PastPattern(verb,person):
    """
    :param verb: 'verb' root verb in phoenician
    :param person: 'person'
    :return:

    """
    if verb[2]=='n':
        return StrongPattern_3n(verb,person)
    elif verb[2]=='y' or verb[2]=='w':
        return WeakPattern_3y__3w(verb,person)
    elif verb[1]=='w' or verb[1]=='y' or (verb[1]=='y' and verb[3]=='n'):
        return WeakPattern_2y__2w__2y_n(verb,person)
    elif verb[1]=='w' and verb[3]=='n':
        return WeakPattern_2w_n(verb,person)
    else:
        return StrongPattern(verb,person)

