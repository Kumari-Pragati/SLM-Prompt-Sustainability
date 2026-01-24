import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(hexagonal_num(0), 0)

    def test_one(self):
        self.assertEqual(hexagonal_num(1), 1)

    def test_negative_numbers(self):
        self.assertEqual(hexagonal_num(-1), -3)
        self.assertEqual(hexagonal_num(-2), -7)
        self.assertEqual(hexagonal_num(-3), -13)

    def test_small_positive_numbers(self):
        self.assertEqual(hexagonal_num(2), 6)
        self.assertEqual(hexagonal_num(3), 12)
        self.assertEqual(hexagonal_num(4), 20)

    def test_large_positive_numbers(self):
        self.assertEqual(hexagonal_num(100), 30201)
        self.assertEqual(hexagonal_num(1000), 3024513)
        self.assertEqual(hexagonal_num(10000), 3024512651)
