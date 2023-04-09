from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog


def test():
    #color = ColorChooser.askcolor(title='Elige un color')
    #print(color)

    #ruta = FileDialog.askopenfilename(title='Abrir un archivo',initialdir='C:', 
    #    filetypes=(('Archivo de texto','*.txt'),('Archivo PDF','*.pdf'),('Todos los archivos','*.*')))
    #print(ruta)

    ruta = FileDialog.asksaveasfile(title='Guardar un archivo') # Equivale a open('ruta','w')
    print(ruta)
    if ruta is not None:
        ruta.write('Hola jeje esto es una prueba')
        ruta.close()

root = Tk()


Button(root,text='Cilcame', command=test).pack()


root.mainloop()