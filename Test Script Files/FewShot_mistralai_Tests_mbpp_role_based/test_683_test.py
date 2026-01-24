import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):
    def test_perfect_square(self):
        self.assertTrue(sum_Square(4))
        self.assertTrue(sum_Square(9))
        self.assertTrue(sum_Square(25))

    def test_non_perfect_square(self):
        self.assertFalse(sum_Square(5))
        self.assertFalse(sum_Square(10))
        self.assertFalse(sum_Square(16))

    def test_zero(self):
        self.assertFalse(sum_Square(0))

    def test_negative_number(self):
        self.assertFalse(sum_Square(-1))
