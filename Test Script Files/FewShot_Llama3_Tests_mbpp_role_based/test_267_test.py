import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_square_sum_positive_numbers(self):
        self.assertEqual(square_Sum(1), 1)

    def test_square_sum_negative_numbers(self):
        self.assertEqual(square_Sum(-1), -1)

    def test_square_sum_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_square_sum_large_numbers(self):
        self.assertEqual(square_Sum(100), 10000)

    def test_square_sum_non_integer_input(self):
        with self.assertRaises(TypeError):
            square_Sum(1.5)
