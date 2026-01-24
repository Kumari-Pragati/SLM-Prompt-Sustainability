import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_square_sum_with_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_square_sum_with_one(self):
        self.assertEqual(square_Sum(1), 6)

    def test_square_sum_with_negative_numbers(self):
        self.assertEqual(square_Sum(-1), 18)
        self.assertEqual(square_Sum(-2), 60)
        self.assertEqual(square_Sum(-3), 147)

    def test_square_sum_with_large_numbers(self):
        self.assertEqual(square_Sum(10), 285)
        self.assertEqual(square_Sum(100), 338350)
        self.assertEqual(square_Sum(1000), 33550336)
