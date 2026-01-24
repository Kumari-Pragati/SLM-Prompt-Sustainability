import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_square_sum_positive_integer(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 8)
        self.assertEqual(square_Sum(3), 38)
        self.assertEqual(square_Sum(4), 98)
        self.assertEqual(square_Sum(5), 185)

    def test_square_sum_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_square_sum_negative_integer(self):
        self.assertEqual(square_Sum(-1), -1)
        self.assertEqual(square_Sum(-2), 32)
        self.assertEqual(square_Sum(-3), 147)
        self.assertEqual(square_Sum(-4), 348)
        self.assertEqual(square_Sum(-5), 665)
