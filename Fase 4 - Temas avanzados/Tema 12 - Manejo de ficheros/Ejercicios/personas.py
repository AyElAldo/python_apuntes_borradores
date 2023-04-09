from io import open

personas = []

try:
    archivo = open('personas.txt','r',encoding = 'utf-8') # encoding = 'utf-8'
    lineas = archivo.readlines()
except FileNotFoundError:
    print("Error! Archivo no encontrado.")
finally:
    archivo.close()


for linea in lineas:
    linea = linea.replace('\n','')
    campos = linea.split(';')
    persona = {'id': campos[0], 'nombre' : campos[1], 'apellido' : campos[2], 'nacimiento' : campos[3]}
    personas.append(persona)

for persona in personas:
    print(f'''
    ID: {int(persona['id']):02d}
    NOMBRE: {persona['nombre']}
    APELLIDO: {persona['apellido']}
    NACIMIENTO: {persona['nacimiento']}
    ''')
    


