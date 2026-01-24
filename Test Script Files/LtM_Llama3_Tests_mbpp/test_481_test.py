import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(is_subset_sum([1, 2, 3], 3, 6))

    def test_simple_invalid(self):
        self.assertFalse(is_subset_sum([1, 2, 3], 3, 7))

    def test_empty_set(self):
        self.assertFalse(is_subset_sum([], 0, 5))

    def test_zero_sum(self):
        self.assertTrue(is_subset_sum([1, 2, 3], 3, 0))

    def test_single_element_set(self):
        self.assertTrue(is_subset_sum([5], 1, 5))

    def test_single_element_set_invalid(self):
        self.assertFalse(is_subset_sum([5], 1, 6))

    def test_multiple_elements_set(self):
        self.assertTrue(is_subset_sum([1, 2, 3, 4], 4, 6))

    def test_multiple_elements_set_invalid(self):
        self.assertFalse(is_subset_sum([1, 2, 3, 4], 4, 7))

    def test_edge_case_set_sum_equal_to_set_sum(self):
        self.assertTrue(is_subset_sum([1, 2, 3, 4], 4, 10))

    def test_edge_case_set_sum_greater_than_set_sum(self):
        self.assertFalse(is_subset_sum([1, 2, 3, 4], 4, 15))
