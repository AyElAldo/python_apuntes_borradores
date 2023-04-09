import unittest

def doblar(a): return a * 2
def sumar(a,b): return a + b 
def es_par(a): return True if a % 2 == 0 else False

class PruebasFunciones(unittest.TestCase):

    def test_doblar(self):
        self.assertEqual(doblar(10),20)
        self.assertEqual(doblar('ab'), 'abab')

    def test_sumar(self):
        self.assertEqual(sumar(10,2), 12)
        self.assertEqual(sumar(-2, 6), 4)

    def test_es_par(self):
        self.assertEqual(es_par(4), True)
        self.assertEqual(es_par(1421), False)

if __name__ == "__main__":

    unittest.main()