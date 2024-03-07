from tkinter import *
from tkinter import messagebox
from datetime import datetime
import pyshorteners

def encurtarUrl():
    if url.get() == '':
        messagebox.showerror('Erro', 'Preencha o campo!')
    else:
        urlOriginal = url.get()
        encurtador = pyshorteners.Shortener()
        novaUrl = encurtador.tinyurl.short(urlOriginal)

        resultado.delete(0, END)
        resultado.insert(0, novaUrl)


janela = Tk()
janela.geometry('500x200')
janela.title('Infinity Shortener')
janela['bg'] = 'white'

titulo = Label(janela, text='Infinity Shortener',
               font='Verdana 15 bold', bg='white', fg='black')
titulo.place(x=150, y=5)

data = Label(janela, text=datetime.now().date(), fg='black',
             font='Verdana 10 bold',)
data.place(x=400, y=5)

texto = Label(janela, text='Insira sua url...',
              font='Verdana 10 bold', fg='black')
texto.place(x=50, y=50)

url = Entry(janela, width=50, bg='lightgrey', font='Verdana 8 bold',
            relief=GROOVE, borderwidth=2, border=2)
url.place(x=50, y=80)

botao = Button(janela, relief=GROOVE, text='Criar',
               font='Verdana 8 bold', bg='black', fg='white',
               command=encurtarUrl)
botao.place(x=410, y=105)

resultado = Entry(janela, font='Verdana 10 bold', fg='black',
                  width=30, relief=GROOVE, borderwidth=2, border=2)
resultado.place(x=50, y=120)



janela.mainloop()


