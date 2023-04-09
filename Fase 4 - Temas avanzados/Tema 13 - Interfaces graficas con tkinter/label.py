from tkinter import *

# Se define un root, se crea el widget
root = Tk()

# Variables dinamicas
texto = StringVar()
texto.set('Nuevo texto desde String Var')


# Titulo de la ventana principal
root.title("Hola Mundo")
# Insertar un icono
root.iconbitmap("./hola.ico")
# Redimensionar en Ancho y Alto respectivamente
root.resizable(True,True)


# Configuración del marco
frame = Frame(root,width=980,height=520)
frame.pack()


################## Uso de etiquetas LABELS ##################

#label = Label(frame, text="Hola mundo!")
# X y Y coordenadas en el widget
#label.place(x=100,y=100)
# PACK empaqueta y distribuye a su manera el tamaño de los widgets
#label.pack()

label = Label(frame,bg='blue',text='Una etiqueta')
label.pack(anchor='nw')
label.config(fg='white',font=('Verdana',20),anchor='nw')
label2 = Label(frame,bg='green',text='Otra etiqueta')
label2.pack(anchor='center')
label3 = Label(frame,bg='red',text='Ultima etiqueta')
label3.pack(anchor='se')

label.config(textvariable=texto)

imagen = PhotoImage(file='./imagen.gif')
label_imagen = Label(frame, image=imagen, bd=0)
label_imagen.pack()

# Ejecuta programa principal
root.mainloop()
