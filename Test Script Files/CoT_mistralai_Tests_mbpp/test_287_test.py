import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_square_sum_positive_integer(self):
        self.assertEqual(square_Sum(1), 6)
        self.assertEqual(square_Sum(2), 28)
        self.assertEqual(square_Sum(3), 81)
        self.assertEqual(square_Sum(4), 144)
        self.assertEqual(square_Sum(5), 230)

    def test_square_sum_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_square_sum_negative_integer(self):
        self.assertEqual(square_Sum(-1), 0)
        self.assertEqual(square_Sum(-2), 0)
        self.assertEqual(square_Sum(-3), 0)

    def test_invalid_input(self):
        self.assertRaises(TypeError, square_Sum, 'not_an_integer')
