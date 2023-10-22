from tkinter import *
import googletrans
import textblob
from PIL import ImageTk,Image
from tkinter import ttk, messagebox

pencere=Tk()
pencere.title('Translator version 2.2.0')
pencere.geometry('1080x400')
pencere.resizable(False,False)
pencere.configure(background='white')


def Secilmis_dili_labele_elave_etmek():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    pencere.after(1000,Secilmis_dili_labele_elave_etmek)

def Tercume_ele():
    text2.delete(1.0, END)

    try:
        for key, value in dil.items():
            if (value == combo1.get()):
                from_language_key = key

        for key, value in dil.items():
            if (value == combo2.get()):
                to_language_key = key

        words = textblob.TextBlob(text1.get(1.0, END))
        words = words.translate(from_lang=from_language_key, to=to_language_key)

        text2.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)



# icon
img1= Image.open("translate-1.jpg")
img1_1=img1.resize((100,100))
img1=ImageTk.PhotoImage(img1_1)
img_label=Label(pencere,image=img1)
pencere.iconphoto(False,img1)

# arrow
img2= Image.open("arrow.png")
img2_2=img2.resize((110,110))
img2=ImageTk.PhotoImage(img2_2)
img_label=Label(pencere,image=img2)
img_label.place(x=472,y=170)

dil=googletrans.LANGUAGES
diller=list(dil.values())


# combobox
combo1=ttk.Combobox(pencere,values=diller,font='Roboto 14',state='r')
# combo1.current(5)
combo1.place(x=110,y=20)
combo1.set('Dili seçin')

label1=Label(pencere,text='ENGLISH',font='segoe 30 bold', bg='white',width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)


combo2=ttk.Combobox(pencere,values=diller,font='Roboto 14',state='r')
combo2.place(x=730,y=20)
combo2.set('Dili seçin')

label2=Label(pencere,text='ENGLISH',font='segoe 30 bold', bg='white',width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

# Sol Frame
frame1=Frame(pencere,bg='black',bd=5)
frame1.place(x=10,y=118,width=430,height=210)

text1=Text(frame1,font='Robote 20',bg='white',relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(frame1)
scrollbar1.pack(side='right',fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Sağ Frame
frame2=Frame(pencere,bg='black',bd=5)
frame2.place(x=620,y=118,width=430,height=210)

text2=Text(frame2,font='Robote 20',bg='white',relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(frame2)
scrollbar2.pack(side='right',fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

# Tərcümə buttonu
btn=Button(pencere,text='Tərcümə et!',font=('Roboto',15),activebackground='red',cursor='hand2',
           bd=1,width=10,height=2,background='yellow',fg='red',command=Tercume_ele)
btn.place(x=476,y=330)


Secilmis_dili_labele_elave_etmek()

pencere.mainloop()











