import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(2), 6)
        self.assertEqual(hexagonal_num(3), 15)
        self.assertEqual(hexagonal_num(4), 24)
        self.assertEqual(hexagonal_num(5), 35)

    def test_zero(self):
        self.assertEqual(hexagonal_num(0), 0)

    def test_negative_integer(self):
        self.assertEqual(hexagonal_num(-1), -1)
        self.assertEqual(hexagonal_num(-2), -12)
        self.assertEqual(hexagonal_num(-3), -21)
        self.assertEqual(hexagonal_num(-4), -30)
        self.assertEqual(hexagonal_num(-5), -45)
