import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositivenum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_single_positive(self):
        self.assertEqual(sum_positivenum([1]), 1)

    def test_multiple_positives(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)

    def test_single_negative(self):
        self.assertEqual(sum_positivenum([-1]), 0)

    def test_multiple_positives_and_negatives(self):
        self.assertEqual(sum_positivenum([1, 2, -3, 4, -5]), 3)

    def test_all_positives(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)

    def test_all_negatives(self):
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5]), 0)

    def test_mixed_positives_and_negatives(self):
        self.assertEqual(sum_positivenum([-1, -2, 3, -4, 5]), 4)
