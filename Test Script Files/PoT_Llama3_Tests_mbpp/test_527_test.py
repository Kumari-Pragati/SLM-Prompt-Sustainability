import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 7), 2)

    def test_edge_case_sum_in_array(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5, 7], 6, 7), 1)

    def test_edge_case_sum_not_in_array(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 10), 0)

    def test_edge_case_single_element_array(self):
        self.assertEqual(get_pairs_count([1], 1, 1), 0)

    def test_edge_case_empty_array(self):
        self.assertEqual(get_pairs_count([], 0, 1), 0)

    def test_edge_case_sum_zero(self):
        self.assertEqual(get_pairs_count([1, 2, 3], 3, 0), 0)

    def test_edge_case_sum_equal_to_first_element(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 1), 0)

    def test_edge_case_sum_equal_to_last_element(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 5), 1)
