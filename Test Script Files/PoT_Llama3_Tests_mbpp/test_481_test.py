import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(is_subset_sum([1, 2, 3], 3, 5))

    def test_edge_case_sum_zero(self):
        self.assertTrue(is_subset_sum([1, 2, 3], 3, 0))

    def test_edge_case_sum_equal_to_set(self):
        self.assertTrue(is_subset_sum([1, 2, 3], 3, 6))

    def test_edge_case_set_empty(self):
        self.assertFalse(is_subset_sum([], 0, 5))

    def test_edge_case_n_zero(self):
        self.assertFalse(is_subset_sum([1, 2, 3], 0, 5))

    def test_edge_case_set_single_element(self):
        self.assertTrue(is_subset_sum([1], 1, 1))

    def test_edge_case_set_single_element_sum_zero(self):
        self.assertTrue(is_subset_sum([1], 1, 0))

    def test_edge_case_set_single_element_sum_greater_than_set(self):
        self.assertFalse(is_subset_sum([1], 1, 2))

    def test_edge_case_set_multiple_elements(self):
        self.assertTrue(is_subset_sum([1, 2, 3], 3, 4))

    def test_edge_case_set_multiple_elements_sum_greater_than_set(self):
        self.assertFalse(is_subset_sum([1, 2, 3], 3, 7))

    def test_edge_case_set_multiple_elements_sum_equal_to_set(self):
        self.assertTrue(is_subset_sum([1, 2, 3], 3, 6))

    def test_edge_case_set_multiple_elements_sum_zero(self):
        self.assertTrue(is_subset_sum([1, 2, 3], 3, 0))

    def test_edge_case_set_invalid_input(self):
        with self.assertRaises(TypeError):
            is_subset_sum('a', 3, 5)
