import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativenum(unittest.TestCase):

    def test_sum_negativenum(self):
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5]), 0)
        self.assertEqual(sum_negativenum([-1, -2, 3, 4, 5]), -3)
        self.assertEqual(sum_negativenum([-1, -2, -3, 4, 5]), -6)
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5, 6]), 0)
        self.assertEqual(sum_negativenum([-1, -2, -3, -4, -5, -6]), -21)
        self.assertEqual(sum_negativenum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0)
        self.assertEqual(sum_negativenum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), -55)
