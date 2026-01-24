import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativenum(unittest.TestCase):
    def test_sum_negativenum(self):
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5]), 0)
        self.assertEqual(sum_negativenum([-1, -2, -3, -4, -5]), -15)
        self.assertEqual(sum_negativenum([1, -2, 3, -4, 5]), -3)
        self.assertEqual(sum_negativenum([-1, 2, -3, 4, -5]), -9)
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0)
        self.assertEqual(sum_negativenum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), -55)
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5, -6, -7, -8, -9, -10]), -25)
        self.assertEqual(sum_negativenum([-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]), -45)
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]), -30)
        self.assertEqual(sum_negativenum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 11, 12, 13, 14, 15]), -75)
