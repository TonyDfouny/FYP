def StrongPattern(verb,person):
    """

    :param verb: 'verb' root verb in phoenician
    :param person: 'person'
    :return:'verb with the correct grammar'
    """
    Pattern={
            "1p.s.c.":"ʾ"+verb,
            "2p.s.m.":"t"+verb,
            "2p.s.f.":"t"+verb,
            "3p.s.m.":"y"+verb,
            "3p.s.f.":"t"+verb,
            "1p.pl.c.":"n"+verb,
            "2p.pl.m.":"t"+verb+"n",
            "2p.pl.f.":"t"+verb+"n",
            "3p.pl.c.":"y"+verb+"n"
             }
    return Pattern[person]

def WeakPattern_1y__ytn(verb,person):
    """

    :param verb: 'verb' root verb in phoenician
    :param person: 'person'
    :return:'verb with the correct grammar'
    """
    Pattern = {
        "1p.s.c.": "ʾ" + verb[1]+verb[2],
        "2p.s.m.": "t" + verb[1]+verb[2],
        "2p.s.f.": "t" + verb[1]+verb[2],
        "3p.s.m.": "y" + verb[1]+verb[2],
        "3p.s.f.": "t" + verb[1]+verb[2],
        "1p.pl.c.": "n" + verb[1]+verb[2],
        "2p.pl.m.": "t" + verb[1]+verb[2]+ "n",
        "2p.pl.f.": "t" + verb[1]+verb[2] + "n",
        "3p.pl.c.": "y" + verb[1]+verb[2] + "n"
    }
    return Pattern[person]

def WeakPattern_2y__2w(verb,person):
    """

    :param verb: 'verb' root verb in phoenician
    :param person: 'person'
    :return:'verb with the correct grammar'
    """
    Pattern = {
        "1p.s.c.": "ʾ" + verb[0] + verb[2],
        "2p.s.m.": "t" + verb[0] + verb[2],
        "2p.s.f.": "t" + verb[0] + verb[2],
        "3p.s.m.": "y" + verb[0] + verb[2],
        "3p.s.f.": "t" + verb[0] + verb[2],
        "1p.pl.c.": "n" + verb[0] + verb[2],
        "2p.pl.m.": "t" + verb[0] + verb[2] + "n",
        "2p.pl.f.": "t" + verb[0] + verb[2] + "n",
        "3p.pl.c.": "y" + verb[0] + verb[2] + "n"
    }
    return Pattern[person]

def WeakPattern_3y(verb,person):
    """

    :param verb: 'verb' root verb in phoenician
    :param person: 'person'
    :return:'verb with the correct grammar'
    """
    Pattern = {
        "1p.s.c.": "ʾ" + verb[0] + verb[1],
        "2p.s.m.": "t" + verb[0] + verb[1],
        "2p.s.f.": "t" + verb[0] + verb[1],
        "3p.s.m.": "y" + verb[0] + verb[1],
        "3p.s.f.": "t" + verb[0] + verb[1],
        "1p.pl.c.": "n" + verb[0] + verb[1],
        "2p.pl.m.": "t" + verb[0] + verb[1] + "n",
        "2p.pl.f.": "t" + verb[0] + verb[1] + "n",
        "3p.pl.c.": "y" + verb[0] + verb[1] + "n"
    }
    return Pattern[person]


def PresentPattern(verb,person):
    """
    :param verb: 'verb' root verb in phoenician
    :param person: 'person'
    :return:

    """
    if verb[0]=='y': ###########YTN?????????#################
        return WeakPattern_1y__ytn(verb,person)
    elif verb[1]=='y' or verb[1]=='w':
        return WeakPattern_2y__2w(verb,person)
    elif verb[2]=='y':
        return WeakPattern_3y(verb,person)
    else:
        return StrongPattern(verb,person)

