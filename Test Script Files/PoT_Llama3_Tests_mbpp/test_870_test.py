import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositivenum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_edge_case_single_positive(self):
        self.assertEqual(sum_positivenum([1]), 1)

    def test_edge_case_single_negative(self):
        self.assertEqual(sum_positivenum([-1]), 0)

    def test_edge_case_all_negative(self):
        self.assertEqual(sum_positivenum([-1, -2, -3, -4, -5]), 0)

    def test_edge_case_mixed_positive_negative(self):
        self.assertEqual(sum_positivenum([-1, 2, -3, 4, -5]), 1)

    def test_edge_case_all_positive(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)

    def test_edge_case_large_list(self):
        self.assertEqual(sum_positivenum([i for i in range(1, 100)]), 4950)
