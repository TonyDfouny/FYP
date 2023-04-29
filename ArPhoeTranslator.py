#GET PARSER#





def TranslateSentence(sourcesentence):
    parsedsentence=ArabicParser(sourcesentence)
    output_sentence=[]
    for words in parsedsentence:
        if words[0]=='V':
            #word = words.split()[1]
            output_sentence.append(TranslateVerb(words))
        else:
            word=words.split()[1]
            output_sentence.append(db[word])