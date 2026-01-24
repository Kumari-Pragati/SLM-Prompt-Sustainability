import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(square_Sum(1), 6)
        self.assertEqual(square_Sum(2), 28)
        self.assertEqual(square_Sum(3), 108)

    def test_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_negative_integer(self):
        self.assertRaises(ValueError, square_Sum, -1)

    def test_large_integer(self):
        self.assertEqual(square_Sum(100), 338350)

    def test_float_input(self):
        self.assertRaises(TypeError, square_Sum, 3.14)
