import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(sum_Square(5))
        self.assertTrue(sum_Square(10))
        self.assertTrue(sum_Square(13))
        self.assertTrue(sum_Square(25))

    def test_negative_numbers(self):
        self.assertFalse(sum_Square(-5))
        self.assertFalse(sum_Square(-10))

    def test_zero(self):
        self.assertFalse(sum_Square(0))

    def test_large_numbers(self):
        self.assertTrue(sum_Square(100))
        self.assertFalse(sum_Square(1000))
