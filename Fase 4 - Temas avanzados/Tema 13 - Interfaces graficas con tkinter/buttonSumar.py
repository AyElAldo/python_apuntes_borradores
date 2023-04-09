from tkinter import *


def sumar():
    resultado.set(float(numero.get()) + float(numero2.get()))
    limpiar()
def restar():
    resultado.set(float(numero.get()) - float(numero2.get()))
    limpiar()
def multiplicar():
    resultado.set(float(numero.get()) * float(numero2.get()))
    limpiar()
def dividir():
    resultado.set(float(numero.get()) / float(numero2.get()))
    limpiar()

def limpiar():
    numero.set('')
    numero2.set('')

root = Tk()
root.config(bd=10)

numero = StringVar()
numero2 = StringVar()
resultado = StringVar()

label = Label(root, text='Numero: ', font=('Arial',20))
label.grid(row=0, column=0)
entry = Entry(root, background='blue', justify='center', textvariable=numero, font=('Arial',20))
entry.grid(row=0, column=1)

label2 = Label(root, text='Numero 2: ', font=('Arial',20))
label2.grid(row=1, column=0)
entry2 = Entry(root, background='red',justify='center', textvariable=numero2, font=('Arial',20))
entry2.grid(row=1, column=1)

label3 = Label(root, text='Resultado: ',font=('Arial',20))
label3.grid(row=2, column=0)
entry3 = Entry(root, background='purple',justify='center', textvariable=resultado, state='disable', font=('Arial',20))
entry3.grid(row=2, column=1)

Label(root,text='  ').grid(row=0,column=2)
Button(root, text='Sumar', command=sumar, font=('Arial',13),bg='gray').grid(row=0, column= 3)
Label(root,text='  ').grid(row=0,column=4)
Button(root, text='Restar', command=restar, font=('Arial',13),bg='gray').grid(row=0, column= 5)
Label(root,text='  ').grid(row=1,column=2)
Button(root, text='Multiplicar', command=multiplicar, font=('Arial',13),bg='gray').grid(row=1, column= 3)
Label(root,text='  ').grid(row=1,column = 4)
Button(root, text='Dividir', command=dividir, font=('Arial',13),bg='gray').grid(row=1, column= 5)



botonSuma = Button(root)

root.mainloop()