# ###### DATABASE #####
#
# # DB={"eat":["verb","akal"],
# #     "word":["type","pheo word"],}
# #
# # DBV={"1p.s.c":"ʾakalti",
# # "2p.s.m":"ʾakalta",
# # "2p.s.f":"ʾakalti",
# # "3p.s m":"ʾakol",
# # "3p.s.f":"ʾékla",
# # "1p.pl.c":"ʾakalnu",
# # "2p.pl.m":"ʾakaltim",
# # "2p.pl.f":"ʾakaltin",
# # "3p.pl.c":"ʾakalū"}
#
#
# ArPhoeDB = {"أنا":"𐤊𐤍𐤀",
# "حمي":"𐤋𐤄𐤀",
# "له":"𐤄",
# "أخت":"𐤕𐤇𐤀",
# "من":"𐤃𐤁",
# "خطير":"𐤌𐤏𐤕𐤔𐤍",
# "حيوانات": "𐤕𐤉𐤇",
# "هو":"𐤀𐤄",
# "اتي":"𐤀𐤁𐤉",
# "مع":"𐤕𐤀" ,
# "له":"𐤅",
# "ابن":"𐤓𐤁",
# "الى":"𐤋" ,
# "بيروت":"𐤕𐤓𐤉𐤁"}
#
#
# VerbDB={
#     #Come
#     "𐤀𐤁𐤉" : {"1p.s.c.":"𐤕𐤀𐤁" ,
#             "3p.s.m.":"𐤉𐤁𐤀" ,
#             "1p.pl.c.":"𐤍𐤀𐤁"},
#     #Protect
#     "𐤋𐤄𐤀": {"1p.s.c." : "𐤕𐤋𐤄𐤀", "3p.s.m." : "𐤋𐤄𐤀", "1p.pl.c.":"𐤍𐤋𐤄𐤀"}
# }
#
# # Sentence1 = " Eng: I protect his sister from dangerous animals ; Ara: أنا أحمي أخته من الحيونات الخطيرة"
# # print("\nSentence1:", Sentence1)
# #
# # Dictionary1 = {"i": "𐤊𐤍𐤀", "protect": "𐤕𐤋𐤄𐤀", "his": "𐤄",
# #                "sister": "𐤕𐤇𐤀", "from": "𐤃𐤁", "dangerous": "𐤌𐤏𐤕𐤔𐤍",
# #                "animals": "𐤕𐤉𐤇"}
# # print("\nTranslation from English to Phoenician: ")
# # print(Dictionary1)
# #
# # Dictionary1 = {"𐤕𐤋𐤄𐤀": {"1p.s.c.": "𐤕𐤋𐤄𐤀", "3p.s.m.": "𐤋𐤄𐤀", "1p.pl.c.": "𐤍𐤋𐤄𐤀"}}
# # print("\nConjugation of the verb protect: ")
# # print(Dictionary1)
# #
# # Dictionary1 = {"أنا": "𐤊𐤍𐤀",
# #
# #                "حمى": "𐤕𐤋𐤄𐤀",
# #                "له": "𐤄",
# #                "أخت": "𐤕𐤇𐤀",
# #                "من": "𐤃𐤁",
# #                "خطير": "𐤌𐤏𐤕𐤔𐤍",
# #                "الحيوانات": "𐤕𐤉𐤇  "}
# # print("\nTranslation form Arabic to Phoenician: ")
# # print(Dictionary1)
# #
# # Sentence2 = " Eng: He comes with his son to Beirut; Ara: هو يأتي مع ابنه الى بيروت "
# # print("\n")
# # print("Sentence2:", Sentence2)
# #
# # Dictionary2 = {"He": "𐤀𐤄", "comes": "𐤕𐤀𐤁", "with": "𐤕𐤀",
# #                "his": "𐤅", "son": "𐤓𐤁", "to": "𐤋", "Beirut": "𐤕𐤓𐤉𐤁"}
# # print("\nTranslation from English to Phoenician: ")
# # print(Dictionary2)
# #
# # Dictionary2 = {"𐤕𐤀𐤁": {"1p.s.c.": "𐤕𐤀𐤁", "3p.s.m.": "𐤀𐤁", "1p.pl.c.": "𐤍𐤀𐤁"}}
# # print("\nConjugation of the verb come: ")
# # print(Dictionary2)
# #
# # Dictionary2 = {"هو": "𐤀𐤄",
# #                "أتى": "𐤕𐤀𐤁",
# #                "مع": "𐤕𐤀",
# #                "له": "𐤅",
# #                "ابن": "𐤓𐤁",
# #                "ل": "𐤋",
# #                "بيروت": "𐤕𐤓𐤉𐤁"}
# # print("\nTrasnlation from Arabic to Phoenician: ")
# # print(Dictionary2)
# #
# # DictionaryEngToPhoe = {"i": "𐤊𐤍𐤀", "protect": "𐤕𐤋𐤄𐤀", "his": "𐤄",
# #                        "sister": "𐤕𐤇𐤀", "from": "𐤃𐤁", "dangerous": "𐤌𐤏𐤕𐤔𐤍",
# #                        "animals": "𐤕𐤉𐤇", "He": "𐤀𐤄", "comes": "𐤕𐤀𐤁", "with": "𐤕𐤀",
# #                        "his": "𐤅", "son": "𐤓𐤁", "to": "𐤋", "Beirut": "𐤕𐤓𐤉𐤁"}
# # print("\nAll the words from English to Phoenician: ")
# # print(DictionaryEngToPhoe)
# #
# # DictionaryAraToPhoe = {"أنا": "𐤊𐤍𐤀",
# #                        "حمى": "𐤕𐤋𐤄𐤀",
# #                        "له": "𐤄",
# #                        "أخت": "𐤕𐤇𐤀",
# #                        "من": "𐤃𐤁",
# #                        "خطير": "𐤌𐤏𐤕𐤔𐤍",
# #                        "الحيوانات": "𐤕𐤉𐤇  ",
# #                        "هو": "𐤀𐤄",
# #                        "أتى": "𐤕𐤀𐤁",
# #                        "مع": "𐤕𐤀",
# #                        "له": "𐤅",
# #                        "ابن": "𐤓𐤁",
# #                        "ل": "𐤋",
# #                        "بيروت": "𐤕𐤓𐤉𐤁"}
# # print("\nAll the words from Arabic to Phoenician: ")
# # print(DictionaryAraToPhoe)
#
# # (`transcript`, `meaning`, `root_t`, `type`,'arabic') VALUES
# #
# #
# liste=[('ytn', 'give,present', 'verb', ''),
# ('bʿlšlm', 'Baʿlšillem', 'proper noun', ''),
# ('bʿnʾ', 'Baʿnaʾ', 'proper noun', ''),
# ('ʿbdʾmn', 'ʿAbdʾAmun', 'proper noun', ''),
# ('ʾšmn', 'ʾEšmun', 'proper noun', ''),
# ('ʿn', 'spring', 'common noun', ''),
# ('ydl', 'Ydll', 'proper noun', ''),
# ('št', 'year', 'common noun', ''),
# ('h', 'his', 'possessive suffix', ''),
# ('ʾp', 'moreover', 'adverb', ''),
# ('ʾršt', 'ʾArišot', 'proper noun', ''),
# ('bt', 'daughter', 'common noun', ''),
# ('ʾšmnytn', 'ʾEšmunyaton', 'proper noun', ''),
# ('ʾḥt', 'sister', 'common noun', ''),
# ('ʾmr', 'say', 'verb', ''),
# ('bš', 'Biša', 'proper noun', ''),
# ('šlm', 'greet', 'verb', ''),
# ('ʾmr', 'word', 'common noun', ''),
# ('šlm', 'pay back', 'verb', ''),
# ('šlm', 'be-well,propser', 'common noun', ''),
# ('bt bt', 'granddaughter', 'common noun', ''),
# ('bt', 'house', 'common noun', ''),
# ('bt', 'temple', 'common noun', ''),
# ('bt ʿlm', 'tomb', 'common noun', ''),
# ('bt ʾlm', 'temple', 'common noun', ''),
# ('bt ʾlnm', 'temples', 'common noun', ''),
# ('bt ʾdn', 'palace,dynasty', 'common noun', ''),
# ('bt ʾb', 'palace,dynasty', 'common noun', ''),
# ('bn bn', 'grandson', 'common noun', ''),
# ('p', 'mouth', 'common noun', ''),
# ('yrḥ', 'month', 'common noun', ''),
# ('yrḥ', 'moon', 'common noun', ''),
# ('ydll', 'Ydll', 'proper noun', ''),
# ('ʿn', 'eye', 'common noun', ''),
# ('ʿnm', 'eyes', 'common noun', ''),
# ('nḥšt', 'bronze', 'common noun', ''),
# ('ʾḥd', 'one', 'number', ''),
# ('ʾḥt', 'one', 'number', ''),
# ('šnm', 'two', 'number', ''),
# ('ʾšnm', 'two', 'number', ''),
# ('šn', 'two', 'number', ''),
# ('ʾšn', 'two', 'number', ''),
# ('štm', 'two', 'number', ''),
# ('št', 'two', 'number', ''),
# ('šlšt', 'three', 'number', ''),
# ('šlš', 'three', 'number', ''),
# ('ʾrbʿt', 'four', 'number', ''),
# ('ʾrbʿ', 'four', 'number', ''),
# ('ḥmšt', 'five', 'number', ''),
# ('ḥmš', 'five', 'number', ''),
# ('ššt', 'six', 'number', ''),
# ('šš', 'six', 'number', ''),
# ('šbʿt', 'seven', 'number', ''),
# ('šbʿ', 'seven', 'number', ''),
# ('šmnt', 'eight', 'number', ''),
# ('šmn', 'eight', 'number', ''),
# ('tsʿt', 'nine', 'number', ''),
# ('tsʿ', 'nine', 'number', ''),
# ('ʿsrt', 'ten', 'number', ''),
# ('ʿsr', 'ten', 'number', ''),
# ('ʿšrm', 'twenty', 'number', ''),
# ('šlšm', 'thirty', 'number', ''),
# ('ʾrbʿm', 'forty', 'number', ''),
# ('ḥmšm', 'fifty', 'number', ''),
# ('ššm', 'sixty', 'number', ''),
# ('šbʿm', 'seventy', 'number', ''),
# ('šmnm', 'eighty', 'number', ''),
# ('tšʿm', 'ninety', 'number', ''),
# ('mʾt', 'one hundred', 'number', ''),
# ('mʾtm', 'two hundred', 'number', ''),
# ('ʾlp', 'one thousand', 'number', ''),
# ('lpny', 'first', 'ordinal number', ''),
# ('lpnt', 'first', 'ordinal number', ''),
# ('šny', 'second', 'ordinal number', ''),
# ('šnt', 'second', 'ordinal number', ''),
# ('rbʿ', 'quarter', 'fraction', ''),
# ('mḥṣ', 'one half', 'fraction', ''),
# ('mḥṣt', 'one half', 'fraction', ''),
# ('ḥṣy', 'one half', 'common noun', ''),
# ('rbʿ šlšt', 'three quarters', 'fraction', ''),
# ('hr', 'mountain', 'common noun', ''),
# ('šr', 'prince', 'common noun', ''),
# ('ʾpy', 'bake', 'verb', ''),
# ('ʾmʿštrt', 'ʾAmʿaštart', 'proper noun', ''),
# ('dʿt', 'knowledge', 'common noun', 'ydʿ'),
# ('hn', 'here', 'preposition', ''),
# ('ypd', 'grief,suffer', 'verb', 'pwd'),
# ('pyd', 'grief,suffer', 'verb', ''),
# ('pwd', 'grief,suffer', 'verb', ''),
# ('ʿzrbʿl', 'ʿAzorbaʿl', 'proper noun', ''),
# ('nšbt', 'settle', 'common noun', 'šbt'),
# ('nḥl', 'possess,inherit', 'verb', ''),
# ('tnḥl', 'possess,inherit', 'verb', 'nḥl'),
# ('mgšt', 'offerings', 'common noun', ''),
# ('mgšh', 'offering', 'common noun', ''),
# ('šbt', 'settle', 'common noun', ''),
# ('bwʾ', 'come', 'verb', ''),
# ('nṭʿ', 'plant', 'verb', ''),
# ('šym', 'put,place', 'verb', ''),
# ('šyt', 'put,place', 'verb', ''),
# ('ḥsp', 'break,split', 'verb', ''),
# ('brk', 'bless', 'verb', ''),
# ('bwʾ', 'bring', 'verb', ''),
# ('ʾry', 'collect', 'verb', ''),
# ('brḥ', 'depart', 'verb', ''),
# ('mḥy', 'eradicate,wipe', 'verb', ''),
# ('pwq', 'find', 'verb', ''),
# ('hpk', 'overturn', 'verb', ''),
# ('ʾrk', 'prolong', 'verb', ''),
# ('ydʿ', 'know', 'verb', ''),
# ('ḥwy', 'live', 'verb', ''),
# ('ʿbt', 'mess', 'verb', ''),
# ('gly', 'move,remove', 'verb', ''),
# ('hlk', 'go', 'verb', ''),
# ('ymm', 'days', 'common noun', 'ym'),
# ('bl', 'Bul', 'proper noun', ''),
# ('pmyytn', 'Pumyyaton', 'proper noun', ''),
# ('kty', 'Kition', 'proper noun', ''),
# ('ʾdyl', 'Idalion', 'proper noun', ''),
# ('tms', 'Tamassos', 'proper noun', ''),
# ('mlkytn', 'Milkyaton', 'proper noun', ''),
# ('mzbḥ', 'altar', 'common noun', ''),
# ('ʾz', 'this', 'determiner', ''),
# ('ʾrwm', 'two lions', 'common noun', 'ʾrw'),
# ('bdʾ', 'Bodo', 'proper noun', ''),
# ('ršpḥṣ', 'Reshep-ḥess (Arrow)', 'proper noun', ''),
# ('yknšlm', 'Yakonshalom', 'proper noun', ''),
# ('ʾšmnʾdn', 'ʾEšmunʾadon', 'proper noun', ''),
# ('ḥṣ', 'arrow', 'common noun', ''),
# ('ʾrw', 'Lion', 'common noun', ''),
# ('mrpʾ', 'Merpa\'', 'proper noun', ''),
# ('smlt', 'image of woman', 'common noun', ''),
# ('yṭnʾ', 'erect', 'verb', 'ṭnʾ'),
# ('m', 'from', 'preposition', ''),
# ('yʾš', 'Yaash', 'proper noun', ''),
# ('ʾšt', 'wife', 'common noun', ''),
# ('bʿltytn', 'Baalatyaton', 'proper noun', ''),
# ('ʿbd', 'servant', 'common noun', ''),
# ('šmʿʾ', 'Shemo', 'proper noun', ''),
# ('bʿlytn', 'Baalyaton', 'proper noun', ''),
# ('rbt', 'mistress', 'common noun', ''),
# ('tšmʿ', 'she listens', 'verb', 'šmʿ'),
# ('ql', 'voice', 'common noun', ''),
# ('ṭnʾ', 'erect', 'verb', ''),
# ('mṣbt', 'stele', 'common noun', ''),
# ('ʾšmnʾdny', 'ʾEšmunʾadony', 'proper noun', ''),
# ('šrdl', 'Šerdel', 'proper noun', ''),
# ('ʿbdmlkrt', 'ʿabdmilkart', 'proper noun', ''),
# ('ršpytn', 'Rešepyaton', 'proper noun', ''),
# ('mlṣ', 'Translator', 'common noun', ''),
# ('krsym', 'thrones', 'common noun', 'krsym'),
# ('krsy', 'throne', 'common noun', ''),
# ('bdʿštrt', 'Bodashtart', 'proper noun', ''),
# ('ṣdn', 'Sidon', 'proper noun', ''),
# ('ym', 'sea', 'common noun', ''),
# ('šmm', 'heaven', 'common noun', ''),
# ('rmm', 'high', 'adjectif', 'rm'),
# ('ʾrṣ', 'land', 'common noun', ''),
# ('ršpm', 'shades,flames', 'common noun', 'ršp'),
# ('mšl', 'rule', 'verb', ''),
# ('šd', 'inland', 'common noun', ''),
# ('qdš', 'saint,holy', 'adjectif', ''),
# ('šd', 'field,farmland', 'common noun', ''),
# ('šd', 'plain', 'common noun', ''),
# ('šd', 'land,region', 'common noun', ''),
# ('rm', 'high', 'adjectif', ''),
# ('ršp', 'shade,flame', 'common noun', ''),
# ('ṣdq', 'legitimate', 'adjectif', ''),
# ('ytnmlk', 'Yatonmilk', 'proper noun', ''),
# ('ṣdq', 'just,right', 'adjectif', ''),
# ('ʾḥṭb', 'Aḥitob', 'proper noun', ''),
# ('qrtḥdšt', 'New City', 'proper noun', ''),
# ('ḥrm', 'Hirom', 'proper noun', ''),
# ('lbnn', 'Lebanon', 'proper noun', ''),
# ('rʾšt', 'choicest', 'adjectif', ''),
# ('qrtḥdšt', 'Carthage', 'proper noun', ''),
# ('ʿbdʾsr', 'ʿAbdʾosir', 'proper noun', ''),
# ('ʿbdssm', 'ʿAbdsasom', 'proper noun', ''),
# ('ḥr', 'ḥor', 'proper noun', ''),
# ('ḥy', 'living', 'common noun', ''),
# ('yṭnʾt', 'erect', 'verb', 'ṭnʾ'),
# ('ʾmtʿštrt', 'ʾAmatʿAštart', 'proper noun', ''),
# ('tʾm', 'Toʾm', 'proper noun', ''),
# ('ʿbdmlk', 'ʿAbdmilk', 'proper noun', ''),
# ('mrqʿ', 'mace', 'common noun', ''),
# ('bʿlrm', 'Baalrom', 'proper noun', ''),
# ('mkl', 'Mikal', 'proper noun', ''),
# ('šmʿ', 'hear,listen', 'verb', ''),
# ('sml', 'image of man', 'common noun', ''),
# ('pʿlt', 'Paʿlot', 'proper noun', ''),
# ('ḥdš', 'renew', 'verb', ''),
# ('ʿzrtbʿl', 'ʿOzertbaʿl', 'proper noun', ''),
# ('mlqrt', 'Milqart', 'proper noun', ''),
# ('pqd', 'administer,oversee', 'verb', ''),
# ('mpqd', 'administrator', 'common noun', ''),
# ('ʾdnšmš', 'ʾAdonšamš', 'proper noun', ''),
# ('smlm', 'statues', 'common noun', 'sml'),
# ('slmt', 'stairs', 'common noun', 'slm'),
# ('ʿbdpmy', 'ʿAbdpoumy', 'proper noun', ''),
# ('ʿbdmlqrt', 'ʿAbdmilqart', 'proper noun', ''),
# ('mpqd', 'administration', 'common noun', ''),
# ('slm', 'staircase', 'common noun', ''),
# ('mpqd', 'tower', 'common noun', ''),
# ('ʾš', 'man', 'common noun', ''),
# ('ʾš', 'fire', 'common noun', ''),
# ('ḥyr', 'ḥayar', 'proper noun', ''),
# ('ptlmys', 'Patlimyos', 'proper noun', ''),
# ('knprs ʾrsnʾs pldlp', 'Kanephoros Arsinoē Philadelphos', 'proper noun', ''),
# ('ʾmtʾsr', 'ʾAmatʾOsir', 'proper noun', ''),
# ('gdʿt', 'Gidʿat', 'proper noun', ''),
# ('btšlm', 'Batšallum', 'proper noun', ''),
# ('mryḥy', 'Maryeḥay', 'proper noun', ''),
# ('ʿbdršp', 'ʿAbdrešep', 'proper noun', ''),
# ('nḥmy', 'Naḥmay', 'common noun', ''),
# ('glb', 'Gallab', 'proper noun', ''),
# ('ndr', 'vow', 'verb', ''),
# ('nm', 'their', 'possessive suffix', ''),
# ('ndr', 'vow', 'common noun', ''),
# ('glb', 'barber', 'common noun', ''),
# ('šlm', 'Šallum', 'proper noun', ''),
# ('ʿnt', 'ʿAnat', 'proper noun', ''),
# ('mʿz', 'force', 'common noun', ''),
# ('ʾdmlkm', 'Lord of kings', 'common noun', ''),
# ('ptlmyš', 'Patlimyoš', 'proper noun', ''),
# ('ssmy', 'Sesmey', 'proper noun', ''),
# ('yqdš', 'consecrate', 'verb', 'qdš'),
# ('mzl', 'luck', 'common noun', ''),
# ('nʿm', 'good,excellent', 'adjectif', ''),
# ('qdš', 'consecrate', 'verb', ''),
# ('qdš', 'inner sanctuary', 'common noun', ''),
# ('qdšt', 'saint,holy', 'adjectif', ''),
# ('nʿm', 'kindness,happiness', 'common noun', ''),
# ('nʿmt', 'good', 'adjectif', ''),
# ('ṣr', 'Tyre', 'proper noun', ''),
# ('ʾḥ', 'brother', 'common noun', ''),
# ('ʾsršmr', 'ʾOsiršamor', 'proper noun', ''),
# ('šyr', 'sing', 'verb', ''),
# ('ʾḥt', 'sister', 'common noun', ''),
# ('nṣḥ', 'conquer,defeat', 'verb', ''),
# ('yṣʾm', 'who came forth', 'common noun', ''),
# ('yṣʾ', 'come forth ', 'verb', ''),
# ('yṣʾ', 'rise (of the sun)', 'verb', ''),
# ('yṣʾ', 'spend,expend money', 'verb', ''),
# ('ʿzr', 'ally', 'common noun', ''),
# ('ʿzr', 'help', 'verb', ''),
# ('ʿzr', 'helper', 'common noun', ''),
# ('ʾt', '', 'accusative particle', ''),
# ('ʾb', 'enemy', 'common noun', ''),
# ('tršš', 'Taršiš', 'proper noun', ''),
# ('grš', 'drive out,expel', 'verb', ''),
# ('šrdn', 'Sardinia', 'proper noun', ''),
# ('ṣbʾ', 'army', 'common noun', ''),
# ('mlktn', 'Milkuton', 'proper noun', ''),
# ('šbn', 'Shabon', 'proper noun', ''),
# ('ngd', 'commander', 'common noun', ''),
# ('pmy', 'Poumay', 'proper noun', ''),
# ('šlm', 'refuge', 'common noun', ''),
# ('brkt', 'bless', 'verb', 'brkt'),
# ('ṣpn', 'Shapon', 'proper noun', ''),
# ('tḥpnḥs', 'Tahpanhas', 'proper noun', ''),
# ('ʾpq', 'get,receive', 'verb', 'pwq'),
# ('šlḥt', 'send', 'verb', 'šlḥ'),
# ('ly', 'to me', 'preposition', 'l'),
# ('tntn', 'give', 'verb', 'ytn'),
# ('mšql', 'shekel', 'common noun', ''),
# ('nqt', 'receipt', 'common noun', ''),
# ('pwq', 'get,receive', 'verb', ''),
# ('šlḥ', 'send', 'verb', ''),
# ('bṭḥ', 'trust', 'verb', ''),
# ('ʿd', 'until', 'preposition', ''),
# ('ʿd', 'even', 'preposition', ''),
# ('bdk', 'in your hand', 'common noun', ''),
# ('bd', 'in the hand', 'common noun', ''),
# ('dbr', 'word,promise', 'common noun', ''),
# ('dbr', 'statement,declaration', 'common noun', ''),
# ('dbr', 'say', 'verb', ''),
# ('dbr', 'tell', 'verb', ''),
# ('bšʾ', 'Bisha\'', 'proper noun', ''),
# ('ʿlt pn', 'in addition to', 'preposition', ''),
# ('pn', 'face', 'common noun', ''),
# ('pn', 'side', 'common noun', ''),
# ('mlʾt', 'give in full', 'verb', 'mlʾ'),
# ('mlʾ', 'give in full', 'verb', ''),
# ('mlʾ', 'fill', 'verb', ''),
# ('ytt', 'give', 'verb', 'ytn'),
# ('ypʿl', 'do', 'verb', 'pʿl'),
# ('ʾdʿ', 'know', 'verb', 'ydʿ'),
# ('ʾtnm', 'ʾEtanim', 'proper noun', ''),
# ('tklt', 'expense', 'common noun', ''),
# ('ʾln', 'god', 'common noun', ''),
# ('qpʾ', 'monetary value', 'common noun', ''),
# ('bnm', 'builders', 'common noun', ''),
# ('kt', 'Kityon', 'proper noun', ''),
# ('prkm', 'taskmasters', 'common noun', ''),
# ('ʾdmm', 'persons', 'common noun', ''),
# ('dl', 'labor', 'common noun', ''),
# ('qṣr', 'monetary unit', 'common noun', ''),
# ('šrm', 'singers', 'common noun', ''),
# ('ʿr', 'city', 'common noun', ''),
# ('šknm', 'dwelling', 'common noun', ''),
# ('mlkt', 'queen', 'common noun', ''),
# ('tklt', 'food storage', 'common noun', ''),
# ('qr', 'monetary value', 'common noun', ''),
# ('nʿrm', 'pages', 'common noun', '')]
# #
#
# import EngArTranslator
# import ArabicParser
# from nltk.stem import arlstem2
# from translators.server import TranslatorError
# stemmer = arlstem2.ARLSTem2()
#
# # Format={
# #     'Transcript':'',
# #     'English':'',
# #     'root_t':'',
# #     'Type':'',
# #     'Oflline':'',
# #     'Stemmed Offline':'',
# #     'Online':'',
# #     'Stemmed Online':'',
# # }
# DATABASE=[]

# """
#     MAKE DATABSE LOOK LIKE :
#     DATABSE=[{'Transcript':'',
#     'English':'',
#     'root_t':'',
#     'Type':'',
#     'Oflline':'',
#     'Stemmed':'',
#     'Online':'',
#     'Stemmed':'',}
#     ,{}
#     ,{}]
#     AND SAVE IT TO DATABSE.txt TO ALWAYS HAVE THE OUTPUT
# """
# t=[['ʾnk', 'I', '', 'personal pronoun', 'انا', 'online =', 'انا'],
#
#     ['tbnt', 'Tabnit', '', 'proper noun', 'Tabnit', 'online =', 'Tabnit'],
#
#     ['khn', 'priest', '', 'common noun', 'كاهن', 'online =', 'كاهن']]
#
# for i in liste:
#     try:
#         Format={}
#         Format['Transcript'] = i[0]
#         Format['English'] = i[1]
#         Format['root_t'] = i[3]
#         Format['Type'] = i[2]
#         Format['Oflline'] = ''#EngArTranslator.TranslateOffline(i[1])
#         Format['Stemmed Offline'] = ''
#         Format['Online'] = ''#EngArTranslator.TranslateOnline(i[1])
#         Format['Stemmed Online']=''
#         DATABASE.append(Format)
#         if Format['Type']=='verb':
#             print(Format,',')
#         #print(Format, ',')
#     except TypeError:
#         pass
#print(DATABASE)
# #
# # for line in DATABASE:
# #     print(line)
#f = open("DATABASE.txt", 'r',encoding='utf-8')
#f.close()
#
#
# import json
# words = open('DATABASE.json','r',encoding='utf-8')
# wordsDB = json.load(words)
# #############VERBS###############
# VERBDATABASE=[]
# for line in wordsDB:
#     if line['Type']=='verb':
#         Format = {}
#         Format['Transcript'] = line['Transcript']
#         Format['English'] = line['English']
#         Format['root_t']=line['root_t']
#         Format['Type'] = line['Type']
#         Format['Oflline'] = line['Oflline']
#         Format['Stemmed Offline'] = line['Stemmed Offline']
#         Format['Online'] = line['Online']
#         Format['Stemmed Online']=line['Stemmed Online']
#         Format['Grammar']='GrammarDict'
#         VERBDATABASE.append(Format)
#
# for i in VERBDATABASE:
#     print(i)

#
# ############ABJAD###############
# abjad=[{'𐤀':'ʾ'},
# {'𐤁':'b'},
# {'𐤂':'g'},
# {'𐤃':'d'},
# {'𐤄':'h'},
# {'𐤅':'w'},
# {'𐤆':'z'},
# {'𐤇':'ḥ'},
# {'𐤈':'ṭ'},
# {'𐤉':'y'},
# {'𐤊':'k'},
# {'𐤋':'l'},
# {'𐤌':'m'},
# {'𐤍':'n'},
# {'𐤎':'s'},
# {'𐤏':'ʿ'},
# {'𐤐':'p'},
# {'𐤑':'ṣ'},
# {'𐤒':'q'},
# {'𐤓':'r'},
# {'𐤔':'š'},
# {'𐤕':'t'},
# ]
#
#
#
#
# # t=[['lpp', 'father', '', 'noun','الدموع','online =']]
# # t[0].append('غادر')
# # print(t[0])
# # print(t[0][5])
# # for i in liste:
# #     i.append('online =')
# #     try:
# #         i.append(EngArTranslator.TranslateOnline(i[1]))
# #     except TranslatorError:
# #         i.append('Error')
# #     if i[3]=='verb':
# #         i[6]=stemmer.stem(i[6])
# #     else:
# #         i[6]=stemmer.norm(i[6])
# #         i[4]=stemmer.norm(i[4])
# #     ar=ArabicParser.ArabicParser(i[4])
# #     if ar[0][:2]=='DT':
# #         i[4]=stemmer.pref(i[4])
# #     ar = ArabicParser.ArabicParser(i[6])
# #     if ar[0][:2] == 'DT':
# #         i[6] = stemmer.pref(i[6])
# #     print(i,',\n')
#
# ####TRY WITH ON TO SE IF 3ALA OR 3ALI
#
# #print(ArabicParser.ArabicParser('الملك'))
# #print(EngArTranslator.TranslateOffline('tear'))
#
# # print(EngArTranslator.TranslateOnline('on'))
# # print(stemmer.norm('على'))
# import json
# words = open('DATABASE.json','r',encoding='utf-8')
# wordsDB = json.load(words)
#
# for line in wordsDB:
#     print(line)

#