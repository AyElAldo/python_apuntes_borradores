import sqlite3

conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()

# RECUPERAR DATOS CON WHERE
cursor.execute("SELECT * FROM usuarios WHERE edad=19")

usuarios = cursor.fetchall()
print(usuarios)


# Cambiar datos con WHERE
cursor.execute('UPDATE usuarios SET nombre="Aldo Santiago" WHERE dni="000000001"')

cursor.execute("SELECT * FROM usuarios WHERE edad=19")

usuarios = cursor.fetchall()
print(usuarios)


# ELIMINAR DATOS CON WHERE
cursor.execute("DELETE FROM usuarios WHERE dni='000000001'")

cursor.execute("SELECT * FROM usuarios WHERE edad=19")

usuarios = cursor.fetchall()
print(usuarios)
conexion.commit()
conexion.close()