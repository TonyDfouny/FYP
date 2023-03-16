#Translator

from Parser import Parser


#source_sentence = " أنا اعطيت تذكار طابع الأبجد الكنعاني للسيدة هدى نجيم مسؤولة المدرسة "
source_sentence="على دلعونة "
source_sentence2="نَحْنُ أَكَلْنَا أسد"
parser = Parser(model_path=r"C:\Users\tony_\Downloads\stanford-corenlp-4.2.0-models-arabic\edu\stanford\nlp\models\lexparser\arabicFactored.ser.gz",
                path_to_jar=r"C:\Users\tony_\Downloads\stanford-parser-4.2.0\stanford-parser-full-2020-11-17\stanford-parser.jar",
                path_to_models_jar=r"C:\Users\tony_\Downloads\stanford-parser-4.2.0\stanford-parser-full-2020-11-17\stanford-parser-4.2.0-models.jar")

result=parser.parse_sentence(source_sentence2)
print(result)

def Translator(source_sentence):
    ####DATABASE####
    DB={"أنا":"𐤀𐤍𐤊",
         "نَحْنُ":"𐤀𐤍𐤇𐤍",
        "أكلت":"𐤀𐤊𐤋𐤕",
        "أَكَلْنَا":"𐤀𐤊𐤋𐤍",
        "أسد":"𐤀𐤓𐤅"
         }

    ar_to_phoe_dict = {}
    for i in source_sentence.split():
        ar_to_phoe_dict[i]=''

    for i in ar_to_phoe_dict.keys():
        if i in DB.keys():
            ar_to_phoe_dict[i]=DB[i]



    ##Target sentence##

    target_sentence=""
    for i in ar_to_phoe_dict.values():
        target_sentence=target_sentence+" "+i

    print(source_sentence,'\n',target_sentence)
    

Translator(source_sentence)
Translator(source_sentence2)
