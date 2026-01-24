import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositiveNum(unittest.TestCase):

    def test_sum_positivenum(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5]), 0)
        self.assertEqual(sum_positivenum([1, -2, 3, -4, 5]), 5)
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5]), 0)
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5, 6]), 21)
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5, -6]), 0)
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5, 6, 7]), 28)
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5, -6, -7]), 0)
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5, 6, 7, 8]), 36)
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5, -6, -7, -8]), 0)
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5, 6, 7, 8, 9]), 45)
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5, -6, -7, -8, -9]), 0)
