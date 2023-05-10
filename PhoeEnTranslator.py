import PhoeVerbFinder
import PhoeWordFinder
import Caribe as cb

def PhoeEnTranslate(sourcesentence):
    """

    :param sourcesentence: source sentence in phoenician
    :return: sentence in english   If * in return means not sure of the word

    """
    outputsentence=''
    words=sourcesentence.split()
    for word in words:
        try:
            outputsentence = outputsentence+' '+PhoeWordFinder.PhoeWordFinder(word).WordFinder()
        except KeyError:
            try:#If it is a verb in StrongPatterns
                outputsentence = outputsentence + ' ' + '*'+PhoeVerbFinder.PhoeVerbFinder(word)
            except KeyError:
                try:#If it start with h(AL)
                    outputsentence = outputsentence + ' ' + '*'+PhoeWordFinder.PhoeWordFinder(word[1:]).WordFinder()
                except KeyError:
                    try:#If it ends with 1 possessive letter (h,..)
                        outputsentence = outputsentence + ' ' + '*'+PhoeWordFinder.PhoeWordFinder(word[:-1]).WordFinder()
                    except KeyError:
                        try:#If it ends with 2 possessive letter (km,..)
                            outputsentence = outputsentence + ' ' + '*'+PhoeWordFinder.PhoeWordFinder(word[-2]).WordFinder()
                        except KeyError:
                            outputsentence = outputsentence + ' ' + word

    #correctedouputsentence=cb.caribe_corrector(outputsentence)
    #return correctedouputsentence
    return outputsentence