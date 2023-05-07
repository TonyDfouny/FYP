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


liste=[

    ['ʾnk', 'I', '', 'personal pronoun', 'انا', 'online =', 'انا'],

    ['tbnt', 'Tabnit', '', 'proper noun', 'Tabnit', 'online =', 'Tabnit'],

    ['khn', 'priest', '', 'common noun', 'كاهن', 'online =', 'كاهن'],

    ['ʿštrt', 'ʿAštart', '', 'proper noun', ' Aštart', 'online =', 'بداية'],

    ['mlk', 'king', '', 'common noun', 'ملك', 'online =', 'ملك'],

    ['ṣdnm', 'Sidonians', '', 'common noun', 'Sidonians', 'online =', 'الصياريون'],

    ['bn', 'son', '', 'common noun', 'ابني', 'online =', 'ابن'],

    ['ʾšmnʿzr', 'ʾEšmunʿazor', '', 'proper noun', 'ʾEšmun azor', 'online =', 'ʾešmunʿazor'],

    ['škb', 'lie down', '', 'verb', 'استلقي', 'online =', 'ضطجع'],

    ['z', 'this', '', 'determiner', None, 'online =', None],

    ['my', 'whoever', '', 'conjunction', 'ايا كان', 'online =', 'ايا كان'],

    ['ʾt', 'you', '', 'personal pronoun', 'انت', 'online =', 'انت'],

    ['kl', 'all', '', 'determiner', 'كل شيء', 'online =', 'الجميع'],

    ['ʾdm', 'man', '', 'common noun', 'رجل', 'online =', 'رجل'],

    ['ʾš', 'who', '', 'determiner', 'الذي', 'online =', 'من'],

    ['tpq', 'find', 'pwq', 'verb', 'تجد', 'online =', 'يجد'],

    ['ʾrn', 'sarcophagus', '', 'common noun', 'Sarcophagus', 'online =', 'تابوت الحجري'],

    ['ʾl', 'do not', '', 'adverb', 'لا', 'online =', 'لا'],

    ['tptḥ', 'open', 'ptḥ', 'verb', 'مفتوحة', 'online =', 'فتح'],

    ['ʿlt', 'upon', '', 'preposition', 'علي', 'online =', 'علي'],

    ['w', 'and', '', 'conjunction', 'و', 'online =', 'و'],

    ['trgz', 'disturb', 'rgz', 'verb', 'اضطراب', 'online =', 'زعج'],

    ['k', 'as', '', 'conjunction', 'as', 'online =', 'مثل'],

    ['h', 'the', '', 'article', 'the', 'online =', 'ال'],

    ['b', 'in', '', 'preposition', 'في', 'online =', 'في'],

    ['y', 'mine', '', 'possessive suffix', 'الغام', 'online =', 'ملكي'],

    ['n', 'me', '', 'personal pronoun', 'انا', 'online =', 'انا'],

    ['ʾy', 'not', '', 'determiner', 'لا', 'online =', 'لا'],

    ['ʾr', 'collect', 'ʾry', 'verb', 'جمع', 'online =', 'جمع'],

    ['ln', 'to us', 'l', 'preposition', 'لنا', 'online =', 'لنا'],
    
    ['ksp', 'silver', '', 'common noun', 'فضة', 'online =', 'فضة'] ,

    ['ḥrṣ', 'gold', '', 'common noun', 'ذهب', 'online =', 'ذهب'] ,
    
    ['mnm', 'whatever', '', 'determiner', 'مهما يكن', 'online =', 'ايا كان'] ,
    
    ['mšd', 'wealth', '', 'common noun', 'ثروة', 'online =', 'ثروة'] ,

    ['blt', 'but', '', 'conjunction', 'لكن', 'online =', 'لكن'] ,
    
    ['tʿbt', 'mess', 'ʿbt', 'verb', 'فوضى', 'online =', 'فوض'] ,
    
    ['dbr', 'matter', '', 'common noun', 'مسالة', 'online =', 'موضوع'] ,
    
    ['hʾ', 'he', '', 'personal pronoun', 'هو', 'online =', 'هو'] ,
    
    ['ʾm', 'if', '', 'conjunction', 'اذا', 'online =', 'لو'] ,
    
    ['ptḥ', 'open', '', 'verb', 'مفتوحة', 'online =', 'فتح'] ,
    
    ['rgz', 'disturb', '', 'verb', 'اضطراب', 'online =', 'زعج'] ,
    
    ['lk', 'to you', 'l', 'preposition', 'لك', 'online =', 'لك'] ,

    ['zrʿ', 'semence,offspring', '', 'common noun', 'حساسية، طفح', 'online =', 'Semence ، ذرية'] ,
    
    ['ḥym', 'living', '', 'common noun', 'معيشة', 'online =', 'معيشة'] ,
    
    ['tḥt', 'under', '', 'preposition', 'تحت بند', 'online =', 'تحت'] ,
    
    ['šmš', 'sun', '', 'common noun', 'شمس', 'online =', 'شمس'] ,
    
    ['mškb', 'rest place', 'škb', 'common noun', 'راحة', 'online =', 'مكان الراحة'] ,
    
    ['rpʾm', 'Old spirits', '', 'common noun', 'ارواح القديمة', 'online =', 'ارواح القديمة'] ,
    
    ['w', 'his', '', 'possessive suffix', 'له', 'online =', 'له'] ,
    
    ['mš', 'statue', '', 'common noun', 'تمثال', 'online =', 'تمثال'] ,
    
    ['bʾ', 'bring', 'bwʾ', 'verb', 'أحضر', 'online =', 'حضر'] ,
    
    ['ʾbbʿl', 'ʾAbibaʿl', '', 'proper noun', 'ʾAbiba l', 'online =', 'ʾabibaʿl'] ,
    
    ['gbl', 'Byblos', '', 'proper noun', 'Byblos', 'online =', 'byblos'] ,
    
    ['yḥmlk', 'Yeḥimilk', '', 'proper noun', 'Yeḥimilk', 'online =', 'ييميلك'] ,
    
    ['mṣrm', 'Egypt', '', 'proper noun', 'مصر', 'online =', 'مصر'] ,
    
    ['l', 'To', '', 'preposition', 'الي', 'online =', 'ل'] ,
    
    ['bʿlt', 'goddess', '', 'proper noun', 'الالهة', 'online =', 'الهة'] ,
    
    ['ʾdt', 'lady', '', 'common noun', 'سيدة', 'online =', 'سيدة'] ,
    
    ['tʾrk', 'prolong', 'ʾrk', 'verb', 'إطالة', 'online =', 'اطال'] ,
    
    ['ymt', 'days', 'ym', 'common noun', 'ايام', 'online =', 'ايام'] ,
    
    ['šnt', 'years', 'št', 'common noun', 'سنوات', 'online =', 'سنين'] ,
    
    ['ʿl', 'on', '', 'preposition', 'on', 'online =', 'علي'] ,
    
    ['pʿl', 'make', '', 'verb', 'جعل', 'online =', 'صنع'] ,
    
    ['ʾlbʿl', 'ʾElibaʿl', '', 'proper noun', 'ʾEliball', 'online =', 'ʾelibaʿl'] ,
    
    ['qr', 'wall', '', 'common noun', 'جدار', 'online =', 'حائط'] ,
    
    ['bny', 'construct,build', '', 'verb', 'بناء', 'online =', 'بناء ، بناء'] ,
    
    ['špṭbʿl', 'Shiptibaal', '', 'proper noun', 'Shiptibaal', 'online =', 'Shiptibaal'] ,
    
    ['ḥnwtm', 'Perfume Autel', 'ḥnwt', 'common noun', 'Perfume Autel', 'online =', 'قال العطور'] ,
    
    ['ʿbdʾšmn', 'ʿAbdʾešmun', '', 'proper noun', ' Abd ešmun', 'online =', 'عبد'] ,
    
    ['bnh', 'constructor', '', 'common noun', 'بناء', 'online =', 'بناء'] ,
    
    ['ʾṣʿʾ', 'ʾIṣaʿʾ', '', 'proper noun', '♪ I aina ♪', 'online =', 'هو'] ,
    
    ['ʾdn', 'master', '', 'common noun', 'سيدي', 'online =', 'يتقن'] ,
    
    ['sml', 'statue', '', 'common noun', 'تمثال', 'online =', 'تمثال'] ,
    
    ['bʿl', 'god', '', 'proper noun', 'الله', 'online =', 'اله'] ,
    
    ['ybrk', 'bless', 'brk', 'verb', 'نعم', 'online =', 'بار'] ,
    
    ['yḥw', 'live', 'ḥwy', 'verb', 'عيش', 'online =', 'عيش'] ,
    
    ['ʾl', 'god', '', 'common noun', 'الله', 'online =', 'اله'] ,
    
    ['ʾl', 'these', '', 'determiner', 'هذه', 'online =', None] ,

    ['kn', 'so', '', 'adverb', 'هكذا', 'online =', 'لذا'] ,

    ['ʾt', 'you', '', 'personal pronoun', 'انت', 'online =', 'انت'] ,

    ['hʾ', 'she', '', 'personal pronoun', 'هي', 'online =', 'هي'] ,

    ['ʾnḥn', 'we', '', 'personal pronoun', 'نحن', 'online =', 'نحن'] ,

    ['ʾtm', 'you', '', 'personal pronoun', 'انت', 'online =', 'انت'] ,

    ['hmt', 'they', '', 'personal pronoun', 'هم', 'online =', 'هم'] ,

    ['plsbʿl', 'Pelsibaʿl', '', 'proper noun', 'Pelsiball', 'online =', 'بيلسيباب'] ,

    ['ʾḥrm', 'ʾAḥirom', '', 'proper noun', 'ʾA irom', 'online =', 'ʾaḥirom'] ,

    ['ʾb', 'father', '', 'common noun', 'ابي', 'online =', 'اب'] ,

    ['št', 'sleeping bed', '', 'common noun', 'نوم', 'online =', 'سرير النوم'] ,

    ['ʿlm', 'eternity', '', 'common noun', 'خلود', 'online =', 'خلود'] ,

    ['mlkm', 'kings', 'mlk', 'common noun', 'ملوك', 'online =', 'ملوك'] ,

    ['skn', 'governor', '', 'common noun', 'حاكم', 'online =', 'محافظ حاكم'] ,

    ['sknm', 'governors', 'skn', 'common noun', 'حكام', 'online =', 'محافظون'] ,

    ['tmʾ', 'commander', '', 'common noun', 'قائد', 'online =', 'قائد'] ,

    ['mḥnt', 'army,camp', '', 'common noun', 'جيش', 'online =', 'مخيم الجيش'] ,

    ['ʿly', 'invade,come up', '', 'verb', 'غزا، تعال', 'online =', 'غزو ، تعال'] ,

    ['ygl', 'move,remove', 'gly', 'verb', 'تحركوا', 'online =', 'تحرك ، ازال'] ,

    ['zn', 'there', '', 'determiner', 'هناك', 'online =', 'هناك'] ,

    ['tḥtsp', 'break,split', 'ḥsp', 'verb', 'استراحة', 'online =', 'كسر ، انقسام'] ,

    ['ḥṭr', 'scepter', '', 'common noun', 'صدر', 'online =', 'صولجان'] ,

    ['mšpṭ', 'royal authority', '', 'common noun', 'سلطة الملكية', 'online =', 'سلطة الملكية'] ,

    ['thtpk', 'overturn', 'hpk', 'verb', 'تراجع', 'online =', 'نقلب'] ,

    ['ksʾ', 'throne', '', 'common noun', 'عرش', 'online =', 'عرش'] ,

    ['nḥt', 'peace', '', 'common noun', 'سلام', 'online =', 'سلام'] ,

    ['tbrḥ', 'depart', 'brḥ', 'verb', 'غادر', 'online =', 'غادر'] ,

    ['ymḥ', 'erase,eradicate,wipe', 'mḥy', 'verb', 'امسحوا , ارقصوا', 'online =', 'محو ، القضاء ، امسح'] ,

    ['spr', 'inscription,document', '', 'common noun', 'inscription,document', 'online =', 'نقش ، وثيقة'] ,

    ['lpp', 'tear', '', 'verb', 'دموع', 'online =', 'قطع'] ,

    ['šbl', 'royal robe', '', 'common noun', 'سرقة ملكية', 'online =', 'رداء الملكي'] ,
    
    ]
    #['ʾyt', '', '', 'accusative particle', ''],

    #['ykn', 'be', 'kwn', 'verb', '...'],

    #['kwn', 'be', '', 'verb', '...'],


import EngArTranslator
import ArabicParser
from nltk.stem import arlstem2
from translators.server import TranslatorError
stemmer = arlstem2.ARLSTem2()

Format={
    'Transcript':'',
    'English':'',
    'root_t':'',
    'Type':'',
    'Oflline':'',
    'Stemmed':'',
    'Online':'',
    'Stemmed':'',
}
DATABASE=[]

"""
    MAKE DATABSE LOOK LIKE :
    DATABSE=[{'Transcript':'',
    'English':'',
    'root_t':'',
    'Type':'',
    'Oflline':'',
    'Stemmed':'',
    'Online':'',
    'Stemmed':'',}
    ,{}
    ,{}]
    AND SAVE IT TO DATABSE.txt TO ALWAYS HAVE THE OUTPUT
"""

for i in liste:
    for j in i:


# t=[['lpp', 'father', '', 'noun','الدموع','online =']]
# t[0].append('غادر')
# print(t[0])
# print(t[0][5])
# for i in liste:
#     i.append('online =')
#     try:
#         i.append(EngArTranslator.TranslateOnline(i[1]))
#     except TranslatorError:
#         i.append('Error')
#     if i[3]=='verb':
#         i[6]=stemmer.stem(i[6])
#     else:
#         i[6]=stemmer.norm(i[6])
#         i[4]=stemmer.norm(i[4])
#     ar=ArabicParser.ArabicParser(i[4])
#     if ar[0][:2]=='DT':
#         i[4]=stemmer.pref(i[4])
#     ar = ArabicParser.ArabicParser(i[6])
#     if ar[0][:2] == 'DT':
#         i[6] = stemmer.pref(i[6])
#     print(i,',\n')

####TRY WITH ON TO SE IF 3ALA OR 3ALI

#print(ArabicParser.ArabicParser('الملك'))
#print(EngArTranslator.TranslateOffline('tear'))

print(EngArTranslator.TranslateOnline('on'))
print(stemmer.norm('على'))