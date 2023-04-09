import sqlite3

conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()


cursor.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(9) UNIQUE,
        nombre VARCHAR(100),
        apeliido VARCHAR(100),
        edad INTEGER
    )
''')

usuarios = [
    ('000000001','Aldo','Santiago',19),
    ('000000002','Haid','Uriarte', 20 ),
    ('000000003','Erik','Garcia', 21)
]

cursor.executemany('INSERT INTO usuarios VALUES (null,?,?,?,?)', usuarios)


conexion.commit()
conexion.close()
