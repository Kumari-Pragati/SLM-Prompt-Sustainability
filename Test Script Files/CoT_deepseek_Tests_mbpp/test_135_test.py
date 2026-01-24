import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(2), 9)
        self.assertEqual(hexagonal_num(3), 20)
        self.assertEqual(hexagonal_num(4), 35)
        self.assertEqual(hexagonal_num(5), 54)

    def test_zero(self):
        self.assertEqual(hexagonal_num(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(hexagonal_num(-1), -1)
        self.assertEqual(hexagonal_num(-2), 5)
        self.assertEqual(hexagonal_num(-3), -14)
        self.assertEqual(hexagonal_num(-4), -29)
        self.assertEqual(hexagonal_num(-5), -44)

    def test_large_numbers(self):
        self.assertEqual(hexagonal_num(100), 19900)
        self.assertEqual(hexagonal_num(1000), 999000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            hexagonal_num('a')
        with self.assertRaises(TypeError):
            hexagonal_num(None)
