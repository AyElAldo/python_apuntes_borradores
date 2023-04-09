from tkinter import *

def hola():
    print('Hola')

def crear_label():
    Label(root, text='Label creada dinamicamente.').pack()

root = Tk()


button = Button(root, text='Clic aqui', command=crear_label)
button.pack()


root.mainloop()