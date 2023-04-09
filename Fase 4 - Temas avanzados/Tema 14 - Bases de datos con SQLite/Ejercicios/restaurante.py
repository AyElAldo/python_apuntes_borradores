import sqlite3

def crear_bd():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL
            )
        """)
    except sqlite3.OperationalError:
        print("La tabla CATEGORIA ya existe")
    else:
        print('La tabla CATEGORIAS se ha creado correctamente.')

    try:
        cursor.execute("""
            CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL,
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY (categoria_id) REFERENCES categoria(id)
            )
        """)
    except sqlite3.OperationalError:
        print("La tabla PLATO ya existe")
    else:
        print('La tabla PLATO se ha creado correctamente.')

    conexion.close()


def agregar_categoria():
    categoria = input('Escribe el nombre de la categoria a agregar: ')

    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()

    try:
        cursor.execute(f"INSERT INTO categoria VALUES(null,'{categoria}')")
    except sqlite3.IntegrityError:
        print('La categoria ya existe.')
    conexion.commit()
    conexion.close()


def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()


    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoria")
    
    opcion_categoria = ""
    while True:
        for categoria in categorias:
            print(f"[{categoria[0]}] {categoria[1]}") 

        try:
            opcion_categoria = int(input("Elige la categoria: "))
        except:
            print("La opcion no es valida. Vuelve a intentarlo.")
        else:
            aux = cursor.execute(f"SELECT * FROM categoria WHERE id={opcion_categoria}")
            opcion_seleccionada = aux.fetchone() 
            print(f"Se ha elegido la opcion [{opcion_seleccionada[0]}] {opcion_seleccionada[1]}")
            break;

    plato = input("Escribe el nombre del nuevo plato: ")

    try:
        cursor.execute(f"INSERT INTO plato VALUES (null,'{plato}', {opcion_categoria})")
    except:
        print(f"El plato {plato} ya existe.")
    else:
        print(f"Plato '{plato}' creado correctamente.")

    conexion.commit()
    conexion.close()

def mostrar_menu():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()

    for categoria in categorias:
        print(f"\t* {categoria[1]}")

        platos = cursor.execute(f"SELECT * FROM plato WHERE categoria_id={categoria[0]}")
        for plato in platos:
            print(f"\t\t- {plato[1]}")

    conexion.commit()
    conexion.close()
    pass


crear_bd()

while True:
    print("\n\t\tBienvenidx al gestor del restaurante!")
    opcion = input('''
        [1] Agregar categoria
        [2] Agregar un plato
        [3] Mostrar Menú
        [4] Salir del programa
        Elige la opcion: ''')


    if opcion == '1':
        agregar_categoria()
    elif opcion == '2':
        agregar_plato()
    elif opcion == '3':
        mostrar_menu()
    elif opcion == '4':
        break
    else:
        print('Opcion incorrecta, vuelve a intentarlo.')