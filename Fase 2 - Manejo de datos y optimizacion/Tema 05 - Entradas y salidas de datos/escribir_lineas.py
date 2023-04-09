import sys

if len(sys.argv) == 3:
    texto = sys.argv[1]
    n = int(sys.argv[2])

    for i in range(n):
        print(texto)
else:
    print("Se necesitan 3 argumentos.")