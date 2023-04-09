from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = ""

# Definicion de funciones
def nuevo():
    global ruta
    mensaje.set('Nuevo archivo.')
    ruta = ""
    texto.delete(1.0, 'end') # Desde 0 no porque es un salto de linea
    root.title(ruta + '- AyElAldo')

def abrir():
    global ruta
    mensaje.set('Abrir archivo.')
    ruta = FileDialog.askopenfilename(
        initialdir='.', 
        filetypes=(('Archivos de texto','*.txt'), ('Archivos LST', '*.lst')),
        title='Abrir archivo de texto')

    if ruta != "":
        archivo = open(ruta, 'r')
        contenido = archivo.read()
        texto.delete(1.0,'end')
        texto.insert('insert',contenido)
        archivo.close()
        root.title(ruta + "- AyElAldo")

def guardar():
    mensaje.set('Guardar archivo.')
    if ruta != "":
        contenido = texto.get(1.0,'end-1c')
        archivo = open(ruta, 'w+')
        archivo.write(contenido)
        archivo.close()
        mensaje.set('El archivo se ha guardado correctamente.')
    else:
        guardarComo()
    
    
def guardarComo():
    global ruta
    mensaje.set('Guardar archivo como...')

    archivo = FileDialog.asksaveasfile(title="Guardar archivo como", 
        mode='w', 
        defaultextension='.txt')

    if archivo != None:
        ruta = archivo.name
        contenido = texto.get(1.0,'end-1c')
        archivo = open(ruta, 'w+')
        archivo.write(contenido)
        archivo.close()
        mensaje.set('El archivo se ha guardado correctamente.')
        root.title(ruta + '- AyElAldo')
    else:
        mensaje.set('No se ha guardado el archivo.')
        ruta = ""


# Configuracion de la raiz
root = Tk()
root.title('Editor de Texto - AyElAldo')


# Menu superior
menubar = Menu(root)


filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Nuevo', command=nuevo)
filemenu.add_command(label='Abrir', command=abrir)
filemenu.add_command(label='Guardar', command=guardar)
filemenu.add_command(label='Guardar como',command=guardarComo)
filemenu.add_separator()
filemenu.add_command(label='Salir', command=root.quit())

menubar.add_cascade(menu=filemenu,label='Archivo')


# Caja de texto central
texto = Text(root,bg='pink',fg='black', 
            selectbackground='black', selectforeground='white',
            bd=5, padx=3,pady=3, font=('Consolas',12))
texto.pack(fill='both', expand=1)

# Monitor inferior
mensaje = StringVar()
mensaje.set('Bienvenido a tu editor.')
monitor = Label(root, textvariable=mensaje, justify='left')
monitor.pack(side='left')


root.config(menu=menubar)

root.mainloop()