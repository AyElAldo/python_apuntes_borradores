import unittest

class Pruebas(unittest.TestCase):
    """Clase usada como una bateria de pruebas que hereda de unittest"""

    def test(self):
        """Metodo que realiza el test"""
        1/0

if __name__ == '__main__':

    unittest.main()
    """Se llama a la bateria de pruebas"""


