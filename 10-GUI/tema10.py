'''
TCL/TK: es un lenguaje de programacion 
componente llamado widget son controles por ejemplo botones input etiquetas
todo esto debe estar contenido

3 geometerias

geometrica pack=

widget label: que crea etiquetas

bg=background
fg=fontcolor

ipadx and ipady = padding
padx and pad = margen
fill = se acondiciona a las paredes
expand = Tryue aplica
side=posiciona el objeto 

label_saludo = tkinter.Label(window, text='hola', bg="red", fg="blue")
label_saludo.pack(ipadx=50, ipady=120)

label_despedida = tkinter.Label(window, text="adios", bg="blue", fg="yellow")
label_despedida.pack(ipadx=80, ipady=150)


Geometria Grid=
Nos sirve para posicionar en un matriz parecida a un excel es decir rejillas
weight nos sirbe para indicar las columnas
columnconfigure(0, weight= 1 )

se tiene que llamar tkt para posicionar
from tkinter import = tkt

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

#USURNAME
usurname_label = ttk.Label(window, text="usurname")
usurname_label.grid(column=0,row=0,sticky=tkinter.W,padx=5,pady=5)

usurname_entry = ttk.Entry(window)
usurname_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5 )

#PASSWORD
password_label = ttk.Label(window, text="password")
password_label.grid(column=0,row=1,sticky=tkinter.W,padx=5,pady=5)

password_entry = ttk.Entry(window, show="*")
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5 )


#BOton
login_button = ttk.Button(window,text="Login")
login_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

login_button = ttk.Button(window,text="Cancel")
login_button.grid(column=1, row=3, sticky=tkinter.W, padx=5, pady=5)

Geometria PLace=
sirve para posicionar de forma absoluta

window = tkinter.Tk()

label1 = tkinter.Label(window,text="Posicionamiento absoluto", bg="blue", fg="red")
label1.place(x=18,y=50)

label1 = tkinter.Label(window,text="Posicionamiento ", bg="blue", fg="red")
label1.place(x=25,y=30)

ejemplo 2

colors = ['blue','red','yellow','purple','white']

for x in range(0,10):
    color = random.randint(0,len(colors)-1)
    color2 = random.randint(0,len(colors)-1)
    label = tkinter.Label(window,text='etiqueta', bg=colors[color],fg=colors[color2])
    label.place(x=random.randint(0,100), y =random.randint(0,100))


relief='sunken' tipo de borde


FRAME


window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

frame = ttk.Frame(window)
label = ttk.Label(frame, text='hola')
label.grid(column=0,row=0, sticky=tkinter.W, padx=50, pady=50)
frame.grid(column='0', row='0', sticky=tkinter.W)


window.mainloop()

LISTA


window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

lista = ['windows','macOS','LINUX','Ms Dos', 'BeOs', 'OS/2']
lista_items = tkinter.StringVar(value = lista)
listbox = tkinter.Listbox(window, height=100, listvariable = lista_items)
listbox.grid(column=0,row=0,sticky=tkinter.W)

window.mainloop()

RADIO BOTTOM

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

seleccionado = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Si", value='1',variable= seleccionado)
r2 = ttk.Radiobutton(window, text="No", value='2',variable= seleccionado)
r3 = ttk.Radiobutton(window, text="Quiza", value='3',variable= seleccionado)

r1.grid(column=0,row=1,pady=5,padx=5)
r2.grid(column=0,row=1,pady=5,padx=5)
r3.grid(column=0,row=1,pady=5,padx=5)

seleccionado2 = tkinter.StringVar()

rs1 = ttk.Radiobutton(window, text='text2',value='12', variable=seleccionado2)



window.mainloop()


CHECKOUT
window = tkinter.Tk()


window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

seleccionado = tkinter.StringVar()
checkbox = ttk.Checkbutton(window, text ='acepto las condiciones', variable = seleccionado, )
checkbox.grid(row=0,column=0)


window.mainloop()


'''



import tkinter


import sys






window = tkinter.Tk()

def saludar(event):
    print('Han hecho click en saludar')

def saludarDobleclick(event):
    print('Han hecho Doble click en saludar')

def salir(event):
    print('Salir')
    window.quit()


boton = tkinter.Button(window, text = 'haz click')
boton.pack()
boton.bind('<Button-1>',saludar)
boton.bind('<Double-1>',saludarDobleclick)

botonSalir = tkinter.Button(window, text = 'Salir')
botonSalir.pack()
botonSalir.bind('<Button-1>',salir)






window.mainloop()

