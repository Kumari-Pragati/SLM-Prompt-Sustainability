import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):

    def test_typical_case(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = 9
        self.assertTrue(is_subset_sum(set, n, sum))

    def test_typical_case_2(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = 30
        self.assertTrue(is_subset_sum(set, n, sum))

    def test_edge_case_sum_zero(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = 0
        self.assertTrue(is_subset_sum(set, n, sum))

    def test_edge_case_set_empty(self):
        set = []
        n = 0
        sum = 10
        self.assertFalse(is_subset_sum(set, n, sum))

    def test_edge_case_sum_greater_than_all_elements(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = 100
        self.assertTrue(is_subset_sum(set, n, sum))

    def test_invalid_input_negative_sum(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = -10
        with self.assertRaises(Exception):
            is_subset_sum(set, n, sum)
