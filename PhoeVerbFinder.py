import PhoeWordFinder

def PhoeVerbFinder(word):
    #If StrongPattern Past:
    try:
        return PhoeWordFinder.Verb(word[-1])
    except KeyError:
        try:
            return PhoeWordFinder.Verb(word[-2])
        except KeyError:
            try:#If StrongPattern Present:
                return PhoeWordFinder.Verb(word[1:])
            except KeyError:
                try:
                    return PhoeWordFinder.Verb(word[1:-1])
                except KeyError:
                    raise KeyError