'''
En este segundo ejercicio, tendréis que crear 
una interfaz sencilla la cual debe de contener 
una lista de elementos seleccionables, 
también debe de tener un label con el 
texto que queráis.


'''
from re import X
import tkinter

from tkinter import ttk

from click import command

def obtener_info():
    print(lista_desplegable.get())

window = tkinter.Tk()
window.title('Lista de elementos')
window.geometry('300x190')


#Lista Desplegable
lista_desplegable = ttk.Combobox(window, width=17)
lista_desplegable.place(x=30,y=77)

#Lista de opciones
tecnologias = ['Python','Php','Html','Java','Javascript']

#INSERTAR VALORES
lista_desplegable['values']=tecnologias


label_bienvenido = tkinter.Label(window, text='Bienvenido')
label_bienvenido.pack(ipadx=50, ipady=120)
label_bienvenido.grid(column=0, row=1, padx=20, pady=5)

label_python = tkinter.Label(window, text='Escoge una tecnologia')
label_python.grid(column=0, row=2, ipadx=70, ipady=5)

window.mainloop()