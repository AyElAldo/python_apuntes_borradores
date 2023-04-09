import sys

if len(sys.argv) == 3:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    if (n < 10 and n > 0) and (m < 10 and m > 0) :
        for i in range(n):
            print()
            for j in range(m):
                print("*",end=" ")
    else:
        print("Los numero deben ser numero enteros positivos entre el 1 y el 9")
else:
    print("--Error en numero de argumentos--")
    print("Debe ejecutarse:  py tabla.py numero1 numero2")