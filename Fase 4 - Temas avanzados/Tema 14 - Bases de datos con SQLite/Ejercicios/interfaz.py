from logging import root
import sqlite3
from tkinter import *

# Configuracion de la raiz
root = Tk()
root.title("AyElAldo´s")
root.resizable(1,1)
root.config(bd=15, relief='groove', bg='orange')

# TITULO Y SUBTITULO
Label(root, text=" AyElAldo´s ", fg='brown', bg='orange',
    font=("Times New Roman", 30, "bold italic"), padx=10, pady=10).pack()

Label(root, text=" Menú del día ", fg='brown', bg='orange',
    font=("Comic sans ms", 20, "bold"), padx=10, pady=10).pack()


# Separacion
Label(root, text="  ", fg='brown', bg='orange',
    font=("Comic sans ms", 10, "bold"), padx=10, pady=10).pack()


# Menu
conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

    # Busqueda de categorias y platos

categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
    Label(root, text=f"-------- {categoria[1]} --------", font=("Comic sans ms",16,"bold"), bg="orange").pack()
    Label(root, text="", bg="orange").pack()
    
    platos = cursor.execute(f"SELECT * FROM plato WHERE categoria_id={categoria[0]}").fetchall()
    for plato in platos:
        Label(root, text=f"{plato[1]}", font=("Comic sans ms", 15), bg="orange").pack()

    Label(root, text="", bg="orange").pack()

conexion.close()



# Loop principal
root.mainloop()
