def doblar(lista):
    """
    Dobla cada numero de una lista

    >>> doblar([1, 2, 3])
    [2, 4, 6]

    >>> doblar([2, 3, 4])
    [4, 6, 8]

    >>> doblar([-2, 5, -1])
    [-4, 10, -2]
    """
    return [numero*2 for numero in lista]


#doblar2 = lambda numero: numero*2
#
#lista = [1,2,3]
#
#resultado = list(map(doblar2,lista))
#
#print(doblar2(4))
#print(resultado)

if __name__ == '__main__':
    import doctest

    doctest.testmod()