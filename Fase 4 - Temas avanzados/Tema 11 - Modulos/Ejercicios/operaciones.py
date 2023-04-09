####################### MÓDULO ###################

def suma(n,m):
    try:
        suma = n + m
        return suma
    except TypeError:
        print("Debes ingresar numeros.")
    finally:
        print("\n")

def resta(n,m):
    try:
        resta = n - m
        return resta
    except TypeError:
        print("Debes ingresar numeros.")
    finally:
        print("\n")

def multiplicacion(n,m):
    try:
        multiplicacion = n * m
        return multiplicacion
    except TypeError:
        print("Debes ingresar numeros.")
    finally:
        print("\n")

def division(n,m):
    try:
        division = n / m
        return division
    except TypeError:
        print("Debes ingresar numeros.")
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    finally:
        print("\n")
