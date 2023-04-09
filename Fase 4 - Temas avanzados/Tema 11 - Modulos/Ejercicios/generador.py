import random
import math

def leer_numero(ini, fin, mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except:
            print("Numero no valido.")
        else:
            if valor >= ini and valor <= fin:
                break

    return valor

def generador():
    numeros = leer_numero(1,20, '¿Cuanto números quieres generar? [1-20]: ')
    modo = leer_numero(1,3,'¿Cómo quieres redondear lo números? \n[1] ALZA\n[2] BAJA \n[3] NORMAL\nOpcion:')

    lista = []
    for i in range(numeros):
        numero = random.uniform(0,101)
        if modo == 1:
            numero_modificado = math.ceil(numero)
            print(f"Normal: {numero} \tModificado: {numero_modificado}")
        elif modo == 2:
            numero_modificado = math.floor(numero)
            print(f"Normal: {numero} \tModificado: {numero_modificado}")
        elif modo == 3:
            numero_modificado = round(numero)
            print(f"Normal: {numero} \tModificado: {numero_modificado}")

        lista.append(numero_modificado)

    return lista


generador()