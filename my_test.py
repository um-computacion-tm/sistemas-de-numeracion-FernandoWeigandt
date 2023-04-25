import unittest
from changeBase import *

class TestBaseChanger(unittest.TestCase):

    def test_baseChanger_dec_all(self):
        self.assertEqual(baseChanger_dec_all(10,2), '1010')
        self.assertEqual(baseChanger_dec_all(15,16), 'F')
        self.assertEqual(baseChanger_dec_all(123,8), '173')

    def test_baseChanger_all_dec(self):
        self.assertEqual(baseChanger_all_dec(1010,2), 10)
        self.assertEqual(baseChanger_all_dec('FF',16), 255)
        self.assertEqual(baseChanger_all_dec(173,8), 123)

    def test_baseChanger_bin_to_oct_and_hex(self):
        self.assertEqual(baseChanger_bin_to_oct_and_hex(1010,8), '12')
        self.assertEqual(baseChanger_bin_to_oct_and_hex(1010,16), 'A')

    def test_baseChanger_oct_to_bin_and_hex(self):
        self.assertEqual(baseChanger_oct_to_bin_and_hex(173,2), '1110111')
        self.assertEqual(baseChanger_oct_to_bin_and_hex(173,16), '7B')

    def test_baseChanger_hex_to_bin_and_oct(self):
        self.assertEqual(baseChanger_hex_to_bin_and_oct('FF',2), '11111111')
        self.assertEqual(baseChanger_hex_to_bin_and_oct('FF',8), '377')

if __name__ == '__main__':
    unittest.main()
