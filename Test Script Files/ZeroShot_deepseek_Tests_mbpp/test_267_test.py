import unittest
from mbpp_267_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 13)
        self.assertEqual(square_Sum(3), 44)
        self.assertEqual(square_Sum(4), 105)

    def test_zero(self):
        self.assertEqual(square_Sum(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(square_Sum(-1), 1)
        self.assertEqual(square_Sum(-2), 13)
        self.assertEqual(square_Sum(-3), 44)
        self.assertEqual(square_Sum(-4), 105)

    def test_large_numbers(self):
        self.assertEqual(square_Sum(10), 1045)
        self.assertEqual(square_Sum(20), 8545)
