'''
En este ejercicio tenéis que crear una lista de RadioButton que muestre 
la opción que se ha seleccionado y que contenga un botón de reinicio para que deje 
todo como al principio.

Al principio no tiene que haber una opción seleccionada.


'''
import tkinter
from tkinter import ttk

windows = tkinter.Tk()

windows.columnconfigure(0,weight=3)
windows.columnconfigure(0,weight=3)

seleccionado = tkinter.StringVar()
r1 =ttk.Radiobutton(windows, text='Perro',value='1',variable = seleccionado)
r2 = ttk.Radiobutton(windows, text='Gato', value='2', variable = seleccionado)
r3 = ttk.Radiobutton(windows, text='Girafa', value='3', variable = seleccionado)
r4 = ttk.Radiobutton(windows, text='Leon',value='4',variable=seleccionado)
r1.grid(column=0,row=1,pady=5,padx=5)
r2.grid(column=0,row=2,pady=5,padx=5)
r3.grid(column=0,row=3,pady=5,padx=5)
r4.grid(column=0,row=4,pady=5,padx=5)

def reset(event):
    print('reiniciar')
    seleccionado.set('0')

boton = tkinter.Button(windows,text= 'reiniciar')

boton.bind('<Button-1>',reset)
boton.grid(column=0,row=4,pady=5,padx=5)

windows.mainloop()
