from tkinter.messagebox import showerror
# import pyttsx3
# import pyperclip
import tkinter
from tkinter import *
from tkinter import ttk
from EngPhoe.EngPhoeTranslator import *
from PhoeEng import PhoeEnTranslator
from EngArPhoe.ArPhoeTranslator import *
from PIL import ImageTk,Image
import tkinter.font as tkFont

def LanguageTranslator():
    root = Tk()
    root.title("Phoenician Translator")
    # root.geometry("1080x400")

    # Icon
    icon = PhotoImage(file='GUI\icon.png')
    root.iconphoto(False, icon)

    # Variables
    inputlanguages = ['English', 'EngAr', 'Phoenician']
    outputlanguages=['English', 'Phoenician']
    # sourcetext=tkinter.StringVar()
    inputlanguage = tkinter.StringVar()
    outputlanguage = tkinter.StringVar()
    # outputtext=tkinter.StringVar()
    online=tkinter.StringVar()
    online.set('Offline')
    # Combobox for input

    inputcombo = ttk.Combobox(root, textvariable=inputlanguage, values=inputlanguages, state='readonly')
    inputcombo.grid(column=10, row=5)

    # TextBox For input
    Label(root, text='Enter your sentence').grid(column=10, row=10)

    # SourceText=Entry(root,textvariable=sourcetext)
    customFont = tkFont.Font(family='Segoe UI Historic', size=14)

    SourceTextBox = Text(root, font=customFont, width=60, height=15)
    SourceTextBox.grid(column=10, row=12)

    # Arrows in the middle
    img = (Image.open(r"GUI\two-way-arrow-icon-14.jpg"))
    resized_image = img.resize((40, 30), Image.ANTIALIAS)
    Arrowimg = ImageTk.PhotoImage(resized_image)
    Arrowbtn = Button(root, image=Arrowimg, state='disabled')
    Arrowbtn.grid(column=12, row=5, rowspan=5)

    # Combobox for Output

    outputcombo = ttk.Combobox(root, textvariable=outputlanguage, values=outputlanguages, state='disabled')
    outputcombo.grid(column=13, row=5)

    # Label for Output
    Label(root, text='Output').grid(column=13, row=10)

    # OutputText=Entry(root,textvariable=outputtext,state='disabled',width=200,height=200)
    OutputTextBox = Text(root, font=customFont, width=60, height=15, state='disabled')
    OutputTextBox.grid(column=13, row=12)

    def InputLanguageSelection(event):
        outputcombo['state'] = 'readonly'
        outputcombo.set('')
        Translatebtn['state'] = 'disabled'
        Arrowbtn['state'] = 'disabled'
        if inputlanguage.get()=='EngAr':
            checkbox['state'] = 'normal'
            outputlanguages.remove('English')
            outputcombo['values'] = outputlanguages
            outputlanguages.append('English')
        elif inputlanguage.get()=='English':
            checkbox['state'] = 'disabled'
            outputlanguages.remove('English')
            outputcombo['values']=outputlanguages
            outputlanguages.append('English')
        elif inputlanguage.get()=='Phoenician':
            checkbox['state'] = 'disabled'
            outputlanguages.remove('Phoenician')
            outputcombo['values'] =outputlanguages
            outputlanguages.append('Phoenician')
    def OutputLanguageSelection(event):
        Translatebtn['state'] = 'normal'
        Arrowbtn['state'] = 'normal'
        # if outputlanguage.get()=='Phoenician':
        #     checkbox['state'] = 'normal'
        # else:
        #     checkbox['state'] = 'disabled'

    inputcombo.bind('<<ComboboxSelected>>', InputLanguageSelection)
    outputcombo.bind('<<ComboboxSelected>>', OutputLanguageSelection)

    def GetText():
        sourcetext = SourceTextBox.get("1.0", "end-1c")
        if ((len(sourcetext)) - (sourcetext.count(' '))) <= 0:
            # showerror('Error','You need to enter a text')
            raise ValueError('You need to enter a text')
        else:
            return sourcetext

    def Translate():
        srclang = inputlanguage.get()
        destlang = outputlanguage.get()
        if srclang == destlang or srclang == 'EngAr' and destlang=='English' or srclang == 'English' and destlang=='EngAr':
            return showerror('Error', "You can't translate to the same language!")
        if srclang == 'EngAr':
            try:
                srctext = GetText()
                OutputTextBox['state'] = 'normal'
                OutputTextBox.delete("1.0", 'end-1c')
                OutputTextBox.insert("1.0", ArPhoeTranslator(srctext,online.get()))
                OutputTextBox['state'] = 'disabled'


            except ValueError:
                return showerror('Error', 'You need to enter a text')
        elif srclang == 'English':
            try:
                srctext = GetText()
                OutputTextBox['state'] = 'normal'
                OutputTextBox.delete("1.0", 'end-1c')
                OutputTextBox.insert("1.0", EngPhoeTranslator.EngPhoeTranslator(srctext).Translate())
                OutputTextBox['state'] = 'disabled'

            except ValueError:
                return showerror('Error', 'You need to enter a text')
        elif srclang=='Phoenician':
            try:
                srctext = GetText()
                OutputTextBox['state'] = 'normal'
                OutputTextBox.delete("1.0", 'end-1c')
                OutputTextBox.insert("1.0", PhoeEnTranslator.PhoeEnTranslate(srctext))
                OutputTextBox['state'] = 'disabled'
            except ValueError:
                return showerror('Error', 'You need to enter a text')
    def ArrowBtn():
        temp = inputlanguage.get()
        inputlanguage.set(outputcombo.get())
        outputcombo.set(temp)
        # newlang = languages
        # # selected = inputlanguage.get()
        # print(newlang[0],newlang[1])
        # newlang.remove(temp)
        # outputcombo['values'] = newlang
        # newlang.append(temp)

    Arrowbtn['command'] = ArrowBtn

    #Check box for online offline
    checkbox=Checkbutton(root,text='Online',variable=online,onvalue='Online',offvalue='Offline',state='disabled')
    checkbox.grid(column=49,row=20)
    # Button Translate
    Translatebtn = Button(root, text='Translate', command=Translate, state='disabled')
    Translatebtn.grid(column=50, row=20)


    # Exit Button
    ExitBtn = Button(root, text='Exit', command=root.destroy)
    ExitBtn.grid(column=100, row=100)


    root.mainloop()



