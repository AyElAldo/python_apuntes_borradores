from io import open 
import sys


# Si no existe, lo crea
archivo = open('contador.txt','a+')
archivo.seek(0)

linea = archivo.readline()

if len(linea) == 0:
    linea = '0'
    archivo.write(linea)

archivo.close()

try:
    contador = int(linea)

    if len(sys.argv) == 2:
        if sys.argv[1] == 'inc':
            contador += 1
        elif sys.argv[1] == 'dec':
            contador -= 1

    print(contador)

    archivo = open('contador.txt','w')
    archivo.write(str(contador))
    archivo.close()
except:
    print("Error! Archivo corrupto")
    
