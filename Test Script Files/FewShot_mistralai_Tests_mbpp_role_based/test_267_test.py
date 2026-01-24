import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 8)
        self.assertEqual(square_Sum(3), 36)
        self.assertEqual(square_Sum(4), 104)
        self.assertEqual(square_Sum(5), 200)

    def test_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_negative_integer(self):
        self.assertEqual(square_Sum(-1), -1)
        self.assertEqual(square_Sum(-2), 16)
        self.assertEqual(square_Sum(-3), 108)
        self.assertEqual(square_Sum(-4), -104)
        self.assertEqual(square_Sum(-5), -200)
