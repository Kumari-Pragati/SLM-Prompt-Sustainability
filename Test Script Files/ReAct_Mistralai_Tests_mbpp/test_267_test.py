import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 8)
        self.assertEqual(square_Sum(10), 380)

    def test_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_negative_integer(self):
        self.assertEqual(square_Sum(-1), -1)
        self.assertEqual(square_Sum(-2), 32)
        self.assertEqual(square_Sum(-10), -380)

    def test_large_integer(self):
        self.assertEqual(square_Sum(1000), 3333333333)

    def test_float(self):
        with self.assertRaises(TypeError):
            square_Sum(3.14)

    def test_string(self):
        with self.assertRaises(TypeError):
            square_Sum('abc')
