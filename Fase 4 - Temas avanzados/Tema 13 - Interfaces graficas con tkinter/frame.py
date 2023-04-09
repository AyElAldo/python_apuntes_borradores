from tkinter import *

# Se define un root, se crea el widget
root = Tk()

# Titulo de la ventana principal
root.title("Hola Mundo")
# Insertar un icono
root.iconbitmap("./hola.ico")
# Redimensionar en Ancho y Alto respectivamente
root.resizable(True,True)



# Crear un marco o FRAME
frame = Frame(root)
# Para empaquetarlo en el root (por defecto centra el frame a lo ancho pero lo deja arriba a lo alto)
frame.pack(side="right", anchor="s")
#### EJEMPLO: Widget con escalable a root
frame.pack(fill='both', expand=1) 
# Configurar tamaño (Se puede pasar directamente al crear el FRAME)
frame.config(width=480,height=320)

######### Estos atributos solo son para el tamaño asignado al crear el frame ###########
# Configuracion de cursor
frame.config(cursor='pirate')
# Fondo
frame.config(bg="lightblue")
# Marco
frame.config(bd=50)
frame.config(relief="sunken")

######### Estos atributos solo son para el root ###########
root.config(cursor='pirate')
# Fondo
root.config(bg="red")
# Marco
root.config(bd=25)
root.config(relief="solid")


# Ejecuta programa principal
root.mainloop()
