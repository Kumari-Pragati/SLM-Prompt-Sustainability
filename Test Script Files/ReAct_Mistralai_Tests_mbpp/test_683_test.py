import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):

    def test_sum_square_positive_numbers(self):
        self.assertTrue(sum_Square(4))
        self.assertTrue(sum_Square(9))
        self.assertTrue(sum_Square(16))

    def test_sum_square_zero(self):
        self.assertFalse(sum_Square(0))

    def test_sum_square_negative_numbers(self):
        self.assertFalse(sum_Square(-1))
        self.assertFalse(sum_Square(-4))
        self.assertFalse(sum_Square(-9))

    def test_sum_square_edge_cases(self):
        self.assertTrue(sum_Square(1))
        self.assertTrue(sum_Square(2))
        self.assertFalse(sum_Square(3))
        self.assertFalse(sum_Square(4))
