import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lab.main import Matrix
class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix()

    def test_get_address(self):
        self.assertEqual(self.matrix.get_adress(3), '1110110010010000')
        self.assertEqual(self.matrix.get_adress(2), '1011111001000000')

    def test_get_word(self):
        self.assertEqual(self.matrix.get_word(2), '0011100000010000')
        self.assertEqual(self.matrix.get_word(3), '0010000000110001')

    def test_insert_word(self):
        self.matrix.insert_word(2, '1100000000000000')
        self.assertEqual(self.matrix.get_word(2), '1100000000000000')

    def test_bitwise_and(self):
        result = self.matrix.bitwise_and(1, 2, 0)
        self.assertEqual(result, '0001000000010000')
        self.assertEqual(self.matrix.get_word(0), '0001000000010000')

    def test_bitwise_nand(self):
        result = self.matrix.bitwise_nand(1, 2, 0)
        self.assertEqual(result, '1110111111101111')
        self.assertEqual(self.matrix.get_word(0), '1110111111101111')

    def test_bitwise_not(self):
        result = self.matrix.bitwise_not(1, 0)
        self.assertEqual(result, '1010111111000011')
        self.assertEqual(self.matrix.get_word(0), '1010111111000011')

    def test_find_closest_above(self):
        result = self.matrix.find_closest_above(7, 4, '1010')
        self.assertEqual(result, 2)

    def test_find_closest_below(self):
        result = self.matrix.find_closest_below(7, 4, '1010')
        self.assertEqual(result, 11)

    def test_summ(self):
        self.matrix.summ('111')
        self.assertEqual(self.matrix.get_word(11), '1001000101010000')

if __name__ == "__main__":
    unittest.main()
