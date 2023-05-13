import PhoeWordFinder

def PhoeVerbFinder(word):
    #If StrongPattern Past:
    try:
        word[-1]
        word[1:]
        word[1:-1]
        word[-2]
    except IndexError:
        raise KeyError
    try:
        return PhoeWordFinder.PhoeWordFinder(word[-1]).VerbFinder()
    except KeyError:
        try:
            return PhoeWordFinder.PhoeWordFinder(word[-2]).VerbFinder()
        except KeyError:
            try:#If StrongPattern Present:
                return PhoeWordFinder.PhoeWordFinder(word[1:]).VerbFinder()
            except KeyError:
                try:
                    return PhoeWordFinder.PhoeWordFinder(word[1:-1]).VerbFinder()
                except KeyError:
                    raise KeyError