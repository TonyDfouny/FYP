###### DATABASE #####

# DB={"eat":["verb","akal"],
#     "word":["type","pheo word"],}
#
# DBV={"1p.s.c":"ʾakalti",
# "2p.s.m":"ʾakalta",
# "2p.s.f":"ʾakalti",
# "3p.s m":"ʾakol",
# "3p.s.f":"ʾékla",
# "1p.pl.c":"ʾakalnu",
# "2p.pl.m":"ʾakaltim",
# "2p.pl.f":"ʾakaltin",
# "3p.pl.c":"ʾakalū"}


ArPhoeDB = {"أنا":"𐤊𐤍𐤀",
"حمي":"𐤋𐤄𐤀",
"له":"𐤄",
"أخت":"𐤕𐤇𐤀",
"من":"𐤃𐤁",
"خطير":"𐤌𐤏𐤕𐤔𐤍",
"الحيوانات": "𐤕𐤉𐤇  ",
"هو":"𐤀𐤄",
"اتي":"𐤀𐤁𐤉",
"مع":"𐤕𐤀" ,
"له":"𐤅",
"ابن":"𐤓𐤁",
"الى":"𐤋" ,
"بيروت":"𐤕𐤓𐤉𐤁"}


VerbDB={
    #Come
    "𐤀𐤁𐤉" : {"1p.s.c.":"𐤕𐤀𐤁" , "3p.s.m.":"𐤀𐤁" , "1p.pl.c.":"𐤍𐤀𐤁"},
    #Protect
    "𐤋𐤄𐤀": {"1p.s.c." : "𐤕𐤋𐤄𐤀", "3p.s.m." : "𐤋𐤄𐤀", "1p.pl.c.":"𐤍𐤋𐤄𐤀"}
}

# Sentence1 = " Eng: I protect his sister from dangerous animals ; Ara: أنا أحمي أخته من الحيونات الخطيرة"
# print("\nSentence1:", Sentence1)
#
# Dictionary1 = {"i": "𐤊𐤍𐤀", "protect": "𐤕𐤋𐤄𐤀", "his": "𐤄",
#                "sister": "𐤕𐤇𐤀", "from": "𐤃𐤁", "dangerous": "𐤌𐤏𐤕𐤔𐤍",
#                "animals": "𐤕𐤉𐤇"}
# print("\nTranslation from English to Phoenician: ")
# print(Dictionary1)
#
# Dictionary1 = {"𐤕𐤋𐤄𐤀": {"1p.s.c.": "𐤕𐤋𐤄𐤀", "3p.s.m.": "𐤋𐤄𐤀", "1p.pl.c.": "𐤍𐤋𐤄𐤀"}}
# print("\nConjugation of the verb protect: ")
# print(Dictionary1)
#
# Dictionary1 = {"أنا": "𐤊𐤍𐤀",
#
#                "حمى": "𐤕𐤋𐤄𐤀",
#                "له": "𐤄",
#                "أخت": "𐤕𐤇𐤀",
#                "من": "𐤃𐤁",
#                "خطير": "𐤌𐤏𐤕𐤔𐤍",
#                "الحيوانات": "𐤕𐤉𐤇  "}
# print("\nTranslation form Arabic to Phoenician: ")
# print(Dictionary1)
#
# Sentence2 = " Eng: He comes with his son to Beirut; Ara: هو يأتي مع ابنه الى بيروت "
# print("\n")
# print("Sentence2:", Sentence2)
#
# Dictionary2 = {"He": "𐤀𐤄", "comes": "𐤕𐤀𐤁", "with": "𐤕𐤀",
#                "his": "𐤅", "son": "𐤓𐤁", "to": "𐤋", "Beirut": "𐤕𐤓𐤉𐤁"}
# print("\nTranslation from English to Phoenician: ")
# print(Dictionary2)
#
# Dictionary2 = {"𐤕𐤀𐤁": {"1p.s.c.": "𐤕𐤀𐤁", "3p.s.m.": "𐤀𐤁", "1p.pl.c.": "𐤍𐤀𐤁"}}
# print("\nConjugation of the verb come: ")
# print(Dictionary2)
#
# Dictionary2 = {"هو": "𐤀𐤄",
#                "أتى": "𐤕𐤀𐤁",
#                "مع": "𐤕𐤀",
#                "له": "𐤅",
#                "ابن": "𐤓𐤁",
#                "ل": "𐤋",
#                "بيروت": "𐤕𐤓𐤉𐤁"}
# print("\nTrasnlation from Arabic to Phoenician: ")
# print(Dictionary2)
#
# DictionaryEngToPhoe = {"i": "𐤊𐤍𐤀", "protect": "𐤕𐤋𐤄𐤀", "his": "𐤄",
#                        "sister": "𐤕𐤇𐤀", "from": "𐤃𐤁", "dangerous": "𐤌𐤏𐤕𐤔𐤍",
#                        "animals": "𐤕𐤉𐤇", "He": "𐤀𐤄", "comes": "𐤕𐤀𐤁", "with": "𐤕𐤀",
#                        "his": "𐤅", "son": "𐤓𐤁", "to": "𐤋", "Beirut": "𐤕𐤓𐤉𐤁"}
# print("\nAll the words from English to Phoenician: ")
# print(DictionaryEngToPhoe)
#
# DictionaryAraToPhoe = {"أنا": "𐤊𐤍𐤀",
#                        "حمى": "𐤕𐤋𐤄𐤀",
#                        "له": "𐤄",
#                        "أخت": "𐤕𐤇𐤀",
#                        "من": "𐤃𐤁",
#                        "خطير": "𐤌𐤏𐤕𐤔𐤍",
#                        "الحيوانات": "𐤕𐤉𐤇  ",
#                        "هو": "𐤀𐤄",
#                        "أتى": "𐤕𐤀𐤁",
#                        "مع": "𐤕𐤀",
#                        "له": "𐤅",
#                        "ابن": "𐤓𐤁",
#                        "ل": "𐤋",
#                        "بيروت": "𐤕𐤓𐤉𐤁"}
# print("\nAll the words from Arabic to Phoenician: ")
# print(DictionaryAraToPhoe)