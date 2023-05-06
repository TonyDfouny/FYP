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
"حيوانات": "𐤕𐤉𐤇",
"هو":"𐤀𐤄",
"اتي":"𐤀𐤁𐤉",
"مع":"𐤕𐤀" ,
"له":"𐤅",
"ابن":"𐤓𐤁",
"الى":"𐤋" ,
"بيروت":"𐤕𐤓𐤉𐤁"}


VerbDB={
    #Come
    "𐤀𐤁𐤉" : {"1p.s.c.":"𐤕𐤀𐤁" , "3p.s.m.":"𐤉𐤁𐤀" , "1p.pl.c.":"𐤍𐤀𐤁"},
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

# (`transcript`, `meaning`, `root_t`, `type`,'arabic') VALUES
liste = [
    ['ʾnk', 'I', '', 'personal pronoun'],

    ['tbnt', 'Tabnit', '', 'proper noun']]
"""

['khn', 'priest', '', 'common noun'] ,

['ʿštrt', 'ʿAštart', '', 'proper noun'] ,

['mlk', 'king', '', 'common noun'] ,

['ṣdnm', 'Sidonians', '', 'common noun'] ,

['bn', 'son', '', 'common noun'] ,

['ʾšmnʿzr', 'ʾEšmunʿazor', '', 'proper noun'] ,

['škb', 'lie down', '', 'verb'] ,

['z', 'this', '', 'determiner'] ,

['my', 'whoever', '', 'conjunction'] ,

['ʾt', 'you', '', 'personal pronoun'] ,

['kl', 'all', '', 'determiner'] ,

['ʾdm', 'man', '', 'common noun'] ,

['ʾš', 'who', '', 'determiner'] ,

['tpq', 'find', 'pwq', 'verb'] ,

['ʾyt', '', '', 'accusative particle'] ,

['ʾrn', 'sarcophagus', '', 'common noun'] ,

['ʾl', 'do not', '', 'adverb'] ,

['tptḥ', 'open', 'ptḥ', 'verb'] ,

['ʿlt', 'upon', '', 'preposition'] ,

['w', 'and', '', 'conjunction'] ,

['trgz', 'disturb', 'rgz', 'verb'] ,

['k', 'as', '', 'conjunction'] ,

['h', 'the', '', 'article'] ,

['b', 'in', '', 'preposition'] ,

['y', 'mine', '', 'possessive suffix'] ,

['n', 'me', '', 'personal pronoun'] ,

['ʾy', 'not', '', 'determiner'] ,

['ʾr', 'collect', 'ʾry', 'verb'] ,

['ln', 'to us', 'l', 'preposition'] ,

['ksp', 'silver', '', 'common noun'] ,

['ḥrṣ', 'gold', '', 'common noun'] ,

['mnm', 'whatever', '', 'determiner'] ,

['mšd', 'wealth', '', 'common noun'] ,

['blt', 'but', '', 'conjunction'] ,

['tʿbt', 'mess', 'ʿbt', 'verb'] ,

['dbr', 'matter', '', 'common noun'] ,

['hʾ', 'he', '', 'personal pronoun'] ,

['ʾm', 'if', '', 'conjunction'] ,

['ptḥ', 'open', '', 'verb'] ,

['rgz', 'disturb', '', 'verb'] ,

['ykn', 'be', 'kwn', 'verb'] ,

['lk', 'to you', 'l', 'preposition'] ,

['zrʿ', 'semence,offspring', '', 'common noun'] ,

['ḥym', 'living', '', 'common noun'] ,

['tḥt', 'under', '', 'preposition'] ,

['šmš', 'sun', '', 'common noun'] ,

['mškb', 'rest place', 'škb', 'common noun'] ,

['rpʾm', 'Old spirits', '', 'common noun'] ,

['w', 'his', '', 'possessive suffix'] ,

['mš', 'statue', '', 'common noun'] ,

['bʾ', 'bring', 'bwʾ', 'verb'] ,

['ʾbbʿl', 'ʾAbibaʿl', '', 'proper noun'] ,

['gbl', 'Byblos', '', 'proper noun'] ,

['yḥmlk', 'Yeḥimilk', '', 'proper noun'] ,

['mṣrm', 'Egypt', '', 'proper noun'] ,

['l', 'To', '', 'preposition'] ,

['bʿlt', 'goddess', '', 'proper noun'] ,

['ʾdt', 'lady', '', 'common noun'] ,

['tʾrk', 'prolong', 'ʾrk', 'verb'] ,

['ymt', 'days', 'ym', 'common noun'] ,

['šnt', 'years', 'št', 'common noun'] ,

['ʿl', 'on', '', 'preposition'] ,

['pʿl', 'make', '', 'verb'] ,

['ʾlbʿl', 'ʾElibaʿl', '', 'proper noun'] ,

['qr', 'wall', '', 'common noun'] ,

['bny', 'construct,build', '', 'verb'] ,

['špṭbʿl', 'Shiptibaal', '', 'proper noun'] ,

['ḥnwtm', 'Perfume Autel', 'ḥnwt', 'common noun'] ,

['ʿbdʾšmn', 'ʿAbdʾešmun', '', 'proper noun'] ,

['bnh', 'constructor', '', 'common noun'] ,

['ʾṣʿʾ', 'ʾIṣaʿʾ', '', 'proper noun'] ,

['ʾdn', 'master', '', 'common noun'] ,

['sml', 'statue', '', 'common noun'] ,

['bʿl', 'god', '', 'proper noun'] ,

['ybrk', 'bless', 'brk', 'verb'] ,

['yḥw', 'live', 'ḥwy', 'verb'] ,

['ʾl', 'god', '', 'common noun'] ,

['ʾl', 'these', '', 'determiner'] ,

['kwn', 'be', '', 'verb'] ,

['kn', 'so', '', 'adverb'] ,

['ʾt', 'you', '', 'personal pronoun'] ,

['hʾ', 'she', '', 'personal pronoun'] ,

['ʾnḥn', 'we', '', 'personal pronoun'] ,

['ʾtm', 'you', '', 'personal pronoun'] ,

['hmt', 'they', '', 'personal pronoun'] ,

['hmt', 'they', '', 'personal pronoun'] ,

['plsbʿl', 'Pelsibaʿl', '', 'proper noun'] ,

['ʾḥrm', 'ʾAḥirom', '', 'proper noun'] ,

['ʾb', 'father', '', 'common noun'] ,

['št', 'sleeping bed', '', 'common noun'] ,

['ʿlm', 'eternity', '', 'common noun'] ,

['mlkm', 'kings', 'mlk', 'common noun'] ,

['skn', 'governor', '', 'common noun'] ,

['sknm', 'governors', 'skn', 'common noun'] ,

['tmʾ', 'commander', '', 'common noun'] ,

['mḥnt', 'army,camp', '', 'common noun'] ,

['ʿly', 'invade,come up', '', 'verb'] ,

['ygl', 'move,remove', 'gly', 'verb'] ,

['zn', 'there', '', 'determiner'] ,

['tḥtsp', 'break,split', 'ḥsp', 'verb'] ,

['ḥṭr', 'scepter', '', 'common noun'] ,

['mšpṭ', 'royal authority', '', 'common noun'] ,

['thtpk', 'overturn', 'hpk', 'verb'] ,

['ksʾ', 'throne', '', 'common noun'] ,

['nḥt', 'peace', '', 'common noun'] ,

['tbrḥ', 'depart', 'brḥ', 'verb'] ,

['ymḥ', 'erase,eradicate,wipe', 'mḥy', 'verb'] ,

['spr', 'inscription,document', '', 'common noun'] ,

['lpp', 'tear', '', 'verb'] ,

['šbl', 'royal robe', '', 'common noun'] 
]"""
import EngArTranslator

for i in liste:
    i.append(EngArTranslator.TranslateOffline(i[1]))
print(liste)