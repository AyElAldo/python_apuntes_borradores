from tkinter import *

def seleccionar():
    monitor.config(text=opcion.get())


def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()

opcion = IntVar()

radiobutton = Radiobutton(root, text='Opcion 1', variable=opcion, value=1, command=seleccionar)
radiobutton.pack()
radiobutton2 = Radiobutton(root, text='Opcion 2', variable=opcion, value=2, command=seleccionar)
radiobutton2.pack()
radiobutton3 = Radiobutton(root, text='Opcion 3', variable=opcion, value=3, command=seleccionar)
radiobutton3.pack()

monitor = Label(root)
monitor.pack()

button_reset = Button(root, text='Reset', command=reset)
button_reset.pack()

root.mainloop()