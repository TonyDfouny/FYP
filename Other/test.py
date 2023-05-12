
from nltk.stem import arlstem2

# words=['ابنه','ابنها','إبنهم','إبنك','كلبنا','كلبكي','كلبكم','كلبي']
# stemmer = arlstem2.ARLSTem2()
# print(stemmer.norm('كاهن'))
"""
customstemmer=arlstem2.CustomARLSTem2()
for word in words:
    #print(stemmer.customsuff(stemmer.norm(word)) )#remove prefix and suffix
    print(customstemmer.possessive(word))
    #print(stemmer.adjective(word))
# print(stemmer.pref('الحيوانات')) ##remove al
# w='الحيوانات'
# print(stemmer.customstem(w))
# print(stemmer.pref(w))
# print(stemmer.custompref(w))
# print(stemmer.stem('ابني'))
# print(customstemmer.possessive('كلبي'))
# print(customstemmer.suff('ابنه'))
# print(stemmer.pref('الحيوان'))
# token='abcdefgh'
# print(token[1:-2] + token[-1])
# print(token[0]+token[-2])
# L=[1,2,'sadsad']
# print(len(L))
"""
# l=[1,3,4,6,7]
# l.remove(4)
# print(l)
# n='tony'
# print(n.count(' '))

# DATABSE={'Transcript':'1',
#     'English':'2',
#     'root_t':'3',
#     'Type':'4',
#     'Oflline':'5',
#     'Stemmed':'6',
#     'Online':'7',
#     'Stemmed':'8',}
#
# for key in DATABSE.keys():
#     i=0
#     print("Format['",key,"']=i[",i,']')
#     i=i+1


# import tkinter as tk
#
# class Application(tk.Frame):
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("300x200")
#
#         tk.Frame.__init__(self, self.root)
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.root.bind('<Return>', self.parse)
#         self.grid()
#
#         self.submit = tk.Button(self, text="Submit")
#         self.submit.bind('<Button-1>', self.parse)
#         self.submit.grid()
#
#     def parse(self, event):
#         print("You clicked?")
#
#     def start(self):
#         self.root.mainloop()
#
#
# Application().start()

# t='tony'
# print(t[1:])

# class Translateclass:
#
#     def __init__(self, sourcesentence, from_code,to_code, translationtype):
#         self.sourcesentence=sourcesentence
#         self.from_code=from_code
#         self.to_code=to_code
#         self.translationtype=translationtype
#
#     def __TranslateOnline(self):
#         """
#         :param sourcesentence: 'sentence in source lang'
#         :param from_code: 'lang code' en for english
#         :param from_code: 'lang code' ar for arabic
#         :return: 'sentence in destination lang'
#         """
#         import translators as ts
#         translatedsentence = ts.translate_text(self.sourcesentence, 'google', self.from_code, self.to_code)
#         return translatedsentence
#
#     def Translate(self):
#         """
#
#         :param sourcesentence: 'sentence in english'
#         :param translationtype: 'offline or online'
#         :return: 'sentence in arabic'
#         """
#
#         if self.translationtype == 'Online':
#             return self.__TranslateOnline()
#
#
# translatedsentence=Translateclass('dog','en','ar','Online')
# print(translatedsentence.Translate())

d = {
            'my': 'y',
            'your': 'k',
            'his': 'h',
            'her': 'h',
            'its': 'h',
            'our': 'n',
            'their': 'm'
        }

d_swap = {v: k for k, v in d.items()}
print(d_swap)