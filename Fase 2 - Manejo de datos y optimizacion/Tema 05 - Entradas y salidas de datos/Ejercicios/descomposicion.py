# [Avanzado] Crea un script llamado descomposicion.py que realice las siguientes tareas:


# Debe tomar 1 argumento que será un número entero positivo.
# En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
# El objetivo del script es descomponer el número en unidades, decenas, centenas, miles...

import sys

if(len(sys.argv) != 2):
    print("--Error en la cantidad de argumentos--")
    print("Debe ejecutarse de la siguiente forma:")
    print("\tpy descomposicion.py numero")
else:
    numero = int(sys.argv[1])

    if(numero < 0):
        print("--Error al introducir el numero--")
        print("Solo se aceptan numeros positivos.")
    else:
        
        cadena = str(numero)
        longitud = len(cadena)

        aux = 1
        for i in range(longitud-1,-1,-1):
            
            print(f"{int(cadena[i])*aux:04d}")

            aux *= 10