from tkinter import *
from tkinter import ttk  # for combo box
from googletrans import Translator, LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1 = text
    src1  = src
    dest1 = dest
    trans = Translator()
    trans1= trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s = combo_src.get()
    d = combo_dest.get()
    msg = Sor_txt.get(1.0,END)
    textget = change(text=msg,src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")  #WXH
root.config(bg='Blue')

lab_txt=Label(root,text="Translator", font=("Time New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)#create a frame

lab_txt=Label(root,text="Source Text", font=("Time New Roman",20,"bold"),fg="black",bg="blue")
lab_txt.place(x=100,y=100,height=20,width=300)

Sor_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=130,height=150,width=480)

#Create combo box
list_text=list (LANGUAGES.values())
combo_src=ttk.Combobox(frame,values=list_text)
combo_src.place(x=10,y=300,height=40,width=150)
combo_src.set("English")

button_change=Button(frame,text="Translate",relief=RAISED, command=data)
button_change.place(x=170,y=300,height=40,width=150)

combo_dest=ttk.Combobox(frame,values=list_text)
combo_dest.place(x=330,y=300,height=40,width=150)
combo_dest.set("English")

#Destination source
lab_txt=Label(root,text="Dest Text", font=("Time New Roman",20,"bold"),fg="black",bg="blue")
lab_txt.place(x=100,y=360,height=20,width=300)

dest_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

root.mainloop()
