import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 3), 2)
        self.assertEqual(get_pairs_count([10, 15, 3, 7, 8], 5, 18), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(get_pairs_count([], 0, 1), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(get_pairs_count([1], 1, 1), 0)

    def test_edge_case_sum_not_found(self):
        self.assertEqual(get_pairs_count([1, 2, 3], 3, 4), 0)

    def test_corner_case_negative_numbers(self):
        self.assertEqual(get_pairs_count([-1, -2, -3, -4, -5], 5, 0), 2)
