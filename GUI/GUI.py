#from tkinter.messagebox import showerror
# import pyttsx3
# import pyperclip
from tkinter import *
from tkinter import ttk


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

#TextBox For input
Label(root,text='Enter your sentence').grid(column=0,row=0)
SourceText=Entry(root)#,textvariable="Enter your sentence")
SourceText.grid(column=0,row=1)

#Logo in the middle



#Exit Button
ExitBtn=Button(root,text='Exit',command=root.destroy)
ExitBtn.grid(column=100,row=100)

root.mainloop()