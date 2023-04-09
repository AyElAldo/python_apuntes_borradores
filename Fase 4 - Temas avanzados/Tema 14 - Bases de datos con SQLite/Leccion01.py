import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()
# Codigo en lenguaje SQL

#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")

#cursor.execute("INSERT INTO usuarios VALUES ('Aldo', 19, 'aldo@santiago.com')")

#cursor.execute("SELECT * FROM usuarios")
#print(cursor)
#usuario = cursor.fetchone()
#print(usuario)


#usuarios = [
#    ('Aldo',19, 'aldo@santiago.com'),
#    ('Haid', 20, 'haid@uriarte.com'),
#    ('Erik', 21, 'erik@dg.com')
#]

#cursor.executemany('INSERT INTO usuarios VALUES (?,?,?)', usuarios)

cursor.execute('SELECT * FROM usuarios')

usuarios = cursor.fetchall()

print(usuarios)


conexion.commit()

conexion.close()