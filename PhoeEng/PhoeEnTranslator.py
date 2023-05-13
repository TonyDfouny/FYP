import PhoeVerbFinder
import PhoeWordFinder
import PhoePossessiveFinder


def PhoeEnTranslate(sourcesentence):
    """

    :param sourcesentence: source sentence in phoenician
    :return: sentence in english   If * in return means not sure of the word

    """
    outputsentence=''
    words=sourcesentence.split()

    for word in words:
        try:
            outputsentence = outputsentence +' ' + PhoeWordFinder.PhoeWordFinder(word).WordFinder()
        except KeyError:
            try:#If it is a verb in StrongPatterns
                outputsentence = outputsentence + ' ' + '*' + PhoeVerbFinder.PhoeVerbFinder(word)
            except KeyError:
                try:
                    if word[0]=='h' or word[0]=='H':#If it start with h(AL)
                        outputsentence = outputsentence + ' ' + 'the ' + PhoeWordFinder.PhoeWordFinder(word[1:]).WordFinder()
                    elif word[0]=='w' or word[0]=='W':#If it start with w
                        outputsentence = outputsentence + ' ' + 'and ' + PhoeWordFinder.PhoeWordFinder(word[1:]).WordFinder()
                    else: # If it ends with possessive letters (h,..)
                        outputsentence = outputsentence + ' ' + PhoePossessiveFinder.PhoePossessiveFinder(word).Translate()
                except KeyError:
                    try:
                        if word[0]=='w' or word[0]=='W':#If it start with wand ends with possessive
                            outputsentence = outputsentence + ' ' + 'and ' + PhoePossessiveFinder.PhoePossessiveFinder(word[1:]).Translate()
                        else:
                            raise KeyError
                    except KeyError:

                        outputsentence = outputsentence + ' ' + word
    #correctedouputsentence=cb.caribe_corrector(outputsentence)
    #return correctedouputsentence
    return outputsentence

