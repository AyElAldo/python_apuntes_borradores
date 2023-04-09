from tkinter import *
from tkinter import messagebox as Messagebox

root = Tk()

def test():
    #Messagebox.showinfo('Hola!','Hola mundo')

    #Messagebox.showwarning('Alerta','Seccion solo para administradores')

    #Messagebox.showerror('Error','Error inesperado')

    #resultado = Messagebox.askquestion('Salir','¿Estas seguro que quieres salir?')
    #if resultado == 'yes':
    #    root.destroy()

    #resultado = Messagebox.askyesno('Salir','¿Estas seguro que quieres salir?')
    #if resultado:
    #    root.destroy()

    #resultado = Messagebox.askokcancel('Salir','¿Estas seguro que quieres salir?')
    #if resultado:
    #    root.destroy()
    
    #resultado = Messagebox.askretrycancel('Salir','¿Estas seguro que quieres salir?')
    #if resultado:
    #    root.destroy()

    pass


Button(root, text='Clicame', command=test).pack()



root.mainloop()