import sqlite3

conexion = sqlite3.connect('usuarios.db')
cursor = conexion.cursor()


# Clave primaria
#
#cursor.execute('''
#    CREATE TABLE usuarios(
#        dni VARCHAR(9) PRIMARY KEY,
#        nombre VARCHAR(100),
#        edad INTEGER,
#        email VARCHAR(100)
#    )
#''')
#
#usuarios = [
#    ('000000001','Aldo',19, 'aldo@santiago.com'),
#    ('000000002','Haid', 20, 'haid@uriarte.com'),
#    ('000000003','Erik', 21, 'erik@dg.com')
#]
#
#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

#cursor.execute('''
#    CREATE TABLE productos (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        nombre VARCHAR(100) NOT NULL,
#        marca VARCHAR(50) NOT NULL,
#        precio FLOAT NOT NULL
#    )
#
#''')


#productos = [
#    ('Teclado', 'Logitech', 19.95),
#    ('Pantalla', 'Hisense', 59.90),
#]
#
#cursor.executemany('INSERT INTO productos VALUES (null,?,?,?)', productos)

cursor.execute('SELECT * FROM productos')

productos = cursor.fetchall()

for producto in productos:
    print(producto)


conexion.commit()
conexion.close()