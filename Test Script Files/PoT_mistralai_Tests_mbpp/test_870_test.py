import unittest
from mbpp_870_code import sum_positivenum

class TestSumPositivenum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_positivenum([1, 2, 3, 4, 5]), 15)

    def test_edge_case_empty_list(self):
        self.assertEqual(sum_positivenum([]), 0)

    def test_edge_case_all_zero(self):
        self.assertEqual(sum_positivenum([0, 0, 0]), 0)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(sum_positivenum([-1, -2, -3]), 0)

    def test_corner_case_single_zero(self):
        self.assertEqual(sum_positivenum([0, 1, 2, 3]), 6)
