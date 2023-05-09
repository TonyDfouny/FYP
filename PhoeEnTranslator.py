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
            outputsentence = outputsentence+' '+PhoeWordFinder.Finder(word)
        except KeyError:
            try:#If it is a verb in StrongPatterns
                outputsentence = outputsentence + ' ' + '*'+PhoeVerbFinder.PhoeVerbFinder(word)
            except KeyError:
                try:#If it start with h(AL)
                    outputsentence = outputsentence + ' ' + '*'+PhoeWordFinder.Finder(word[1:])
                except KeyError:
                    try:#If it ends with 1 possessive letter (h,..)
                        outputsentence = outputsentence + ' ' + '*'+PhoeWordFinder.Finder(word[:-1])
                    except KeyError:
                        try:#If it ends with 2 possessive letter (h,..)
                            outputsentence = outputsentence + ' ' + '*'+PhoeWordFinder.Finder(word[:-2])
                        except KeyError:
                            outputsentence = outputsentence + ' ' + word

    #correctedouputsentence=cb.caribe_corrector(outputsentence)
    #return correctedouputsentence
    return outputsentence