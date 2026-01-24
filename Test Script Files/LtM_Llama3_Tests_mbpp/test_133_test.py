import unittest
from mbpp_133_code import sum_negativenum

class TestSumNegativenum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_negativenum([]), 0)

    def test_single_positive(self):
        self.assertEqual(sum_negativenum([1]), 0)

    def test_single_negative(self):
        self.assertEqual(sum_negativenum([-1]), -1)

    def test_multiple_positives(self):
        self.assertEqual(sum_negativenum([1, 2, 3]), 0)

    def test_multiple_negatives(self):
        self.assertEqual(sum_negativenum([-1, -2, -3]), -6)

    def test_mixed_positives_and_negatives(self):
        self.assertEqual(sum_negativenum([1, -2, 3, -4]), -3)

    def test_edge_case_single_zero(self):
        self.assertEqual(sum_negativenum([0]), 0)

    def test_edge_case_single_maxint(self):
        self.assertEqual(sum_negativenum([2147483647]), 0)

    def test_edge_case_single_minint(self):
        self.assertEqual(sum_negativenum([-2147483648]), -2147483648)
