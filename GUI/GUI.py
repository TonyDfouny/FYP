from tkinter.messagebox import showerror
# import pyttsx3
# import pyperclip
import tkinter
from tkinter import *
from tkinter import ttk
from ArPhoeTranslator import *

# class LanguageTranslator:
#     def __init__(self, master):
#         self.master = master
#         self.MainWindow()
#         #self.Widgets()
#     def MainWindow(self):
#         #self.master.geometry('600x430+300+150')
#         self.master.title('Language Translator')
#         #self.master.resizable(width=0, height=0)
#     def Widgets(self):
#         self.master.
#
#
#
# #root =(themename="cosmo")
# root=Tk()
# application = LanguageTranslator(root)
# root.mainloop()

# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()




root=Tk()
root.title("Phoenician Translator")
#root.geometry("1080x400")

#Variables
languages=['English','Phoenician']
sourcetext=tkinter.StringVar()
inputlanguage=tkinter.StringVar()
outputlanguage=tkinter.StringVar()
outputtext=tkinter.StringVar()

#Combobox for input

inputcombo=ttk.Combobox(root,textvariable=inputlanguage,values=languages,state='readonly')
inputcombo.grid(column=10,row=5)
#TextBox For input
Label(root,text='Enter your sentence').grid(column=10,row=10)
SourceText=Entry(root,textvariable=sourcetext)
SourceText.grid(column=10,row=12)

#Logo in the middle
Label(root,text='two arrows goes here').grid(column=12,row=10)

#Combobox for Output

outputcombo=ttk.Combobox(root,textvariable=outputlanguage,state='disabled')
outputcombo.grid(column=13,row=5)
#Label for Output
Label(root,text='Output').grid(column=13,row=10)
OutputText=Label(root,textvariable=outputtext)
OutputText.grid(column=13,row=11)










#Language Selection
def InputLanguageSelection(event):
    newlang = languages
    selected=inputlanguage.get()
    newlang.remove(selected)
    outputcombo['values']=newlang
    outputcombo['state']='readonly'
    newlang.append(selected)

def OutputLanguageSelection(event):
    Translatebtn['state']='normal'

inputcombo.bind('<<ComboboxSelected>>', InputLanguageSelection)
outputcombo.bind('<<ComboboxSelected>>', OutputLanguageSelection)

def GetText():
    if ((len(sourcetext.get()))-(sourcetext.get().count(' ')))<=0:
        showerror('Error','You need to enter a text')
    else:
        return sourcetext.get()


def LanguageSelection():
    srclang=inputlanguage.get()
    destlang=outputlanguage.get()
    if srclang=='English':
        srctext=GetText()
        outputtext.set(ArPhoeTranslator(srctext))




#Button Translate
Translatebtn=Button(root,text='Translate',command=LanguageSelection,state='disabled')
Translatebtn.grid(column=50,row=20)

#Exit Button
ExitBtn=Button(root,text='Exit',command=root.destroy)
ExitBtn.grid(column=100,row=100)

root.mainloop()