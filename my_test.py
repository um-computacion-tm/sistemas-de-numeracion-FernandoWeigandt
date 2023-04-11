import unittest
from changeBase import *

class TestBaseChanger(unittest.TestCase):
    def test_1(self):
        resultado = baseChanger_dec_bin(2)
        self.assertEqual(resultado, 1010)


if __name__== '__main__':
    unittest.main()


