def suma(a,b):
    """
    La función suma(a,b) devuelve la suma de dos numeros.
    
    >>> suma(10,5)
    15
    
    """
    
    return a+b

if __name__ == '__main__':

    import doctest

    doctest.testmod()