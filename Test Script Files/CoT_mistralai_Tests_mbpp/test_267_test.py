import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_square_sum_positive_integer(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 8)
        self.assertEqual(square_Sum(3), 30)
        self.assertEqual(square_Sum(4), 64)
        self.assertEqual(square_Sum(5), 100)

    def test_square_sum_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_square_sum_negative_integer(self):
        self.assertEqual(square_Sum(-1), -1)
        self.assertEqual(square_Sum(-2), 16)
        self.assertEqual(square_Sum(-3), -30)
        self.assertEqual(square_Sum(-4), -64)
        self.assertEqual(square_Sum(-5), -100)

    def test_invalid_input(self):
        self.assertRaises(TypeError, square_Sum, 'str')
        self.assertRaises(TypeError, square_Sum, 0.5)
        self.assertRaises(TypeError, square_Sum, -3.5)
