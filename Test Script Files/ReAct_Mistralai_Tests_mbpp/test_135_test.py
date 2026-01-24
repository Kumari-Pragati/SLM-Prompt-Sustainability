import unittest
from mbpp_135_code import hexagonal_num

class TestHexagonalNum(unittest.TestCase):

    def test_positive_integer(self):
        """Test hexagonal number for positive integers"""
        self.assertEqual(hexagonal_num(1), 1)
        self.assertEqual(hexagonal_num(2), 6)
        self.assertEqual(hexagonal_num(3), 15)
        self.assertEqual(hexagonal_num(10), 221)

    def test_zero(self):
        """Test hexagonal number for zero"""
        self.assertEqual(hexagonal_num(0), 0)

    def test_negative_integer(self):
        """Test hexagonal number for negative integers"""
        self.assertEqual(hexagonal_num(-1), -1)
        self.assertEqual(hexagonal_num(-2), 5)
        self.assertEqual(hexagonal_num(-3), 15)
        self.assertEqual(hexagonal_num(-10), -221)

    def test_large_integer(self):
        """Test hexagonal number for large integers"""
        self.assertEqual(hexagonal_num(100), 30646)
        self.assertEqual(hexagonal_num(1000), 2979019)
