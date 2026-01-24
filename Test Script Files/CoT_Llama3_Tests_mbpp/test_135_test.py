import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(2), 3)
        self.assertEqual(hexagonal_num(3), 7)
        self.assertEqual(hexagonal_num(4), 9)
        self.assertEqual(hexagonal_num(5), 15)

    def test_negative_numbers(self):
        with self.assertRaises(TypeError):
            hexagonal_num(-1)

    def test_zero(self):
        self.assertEqual(hexagonal_num(0), 0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            hexagonal_num(1.5)

    def test_large_numbers(self):
        self.assertEqual(hexagonal_num(100), 9901)
