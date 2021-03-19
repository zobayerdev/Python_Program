#import library
from tkinter import*
from translate import Translator
from tkinter import ttk
#translation
def translate():

 ip=engVariable.get()

 langauge=lang.get()

 translator = Translator(to_lang=langauge)

 translation = translator.translate(ip)

 transVariable.set(translation)


root =Tk()

root.geometry("700x200")

root["bg"]="#20325B"

root.title("ZHN:Language Translator")

global engVariable
global transVariable
global lang;
engVariable=StringVar()
transVariable=StringVar()
lang=StringVar()

Entry(root,text="Hello",textvariable=engVariable,font="Arial 12",fg="black",width=42).place(x=80,y=30)

fontExample = ("Courier", 12, "bold")
comboExample = ttk.Combobox(root,textvariable=lang,
                            values=[
                                    "German",
                                    "Chinese",
                                    "Japanese"],

                            font = fontExample)

root.option_add('*TCombobox*Listbox.font', fontExample)
comboExample.place(x=80,y=70)


Button(root,text="Translate",font="Arial 12 bold",width="10",command=translate,bg="orange").place(x=350,y=70)

Label(root,text="Hello",textvariable=transVariable,font="Arial 12",bg="#20325B",fg="white").place(x=80,y=120)
root.mainloop()