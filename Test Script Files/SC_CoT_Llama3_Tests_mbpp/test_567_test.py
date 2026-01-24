import unittest
from mbpp_567_code import issort_list

class TestIssortList(unittest.TestCase):
    def test_typical_input(self):
        self.assertTrue(issort_list([1, 2, 3, 4, 5]))

    def test_edge_case_decreasing(self):
        self.assertTrue(issort_list([5, 4, 3, 2, 1]))

    def test_edge_case_increasing(self):
        self.assertTrue(issort_list([1, 2, 3, 4, 5]))

    def test_edge_case_single_element(self):
        self.assertTrue(issort_list([1]))

    def test_edge_case_empty_list(self):
        self.assertTrue(issort_list([]))

    def test_edge_case_single_element_descending(self):
        self.assertTrue(issort_list([5]))

    def test_edge_case_single_element_ascending(self):
        self.assertTrue(issort_list([1]))

    def test_edge_case_all_equal(self):
        self.assertTrue(issort_list([1, 1, 1, 1, 1]))

    def test_edge_case_all_equal_descending(self):
        self.assertTrue(issort_list([5, 5, 5, 5, 5]))

    def test_edge_case_all_equal_ascending(self):
        self.assertTrue(issort_list([1, 1, 1, 1, 1]))

    def test_edge_case_reversed(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))

    def test_edge_case_reversed_descending(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))

    def test_edge_case_reversed_ascending(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))

    def test_edge_case_all_negative(self):
        self.assertTrue(issort_list([-5, -4, -3, -2, -1]))

    def test_edge_case_all_negative_descending(self):
        self.assertTrue(issort_list([-5, -4, -3, -2, -1]))

    def test_edge_case_all_negative_ascending(self):
        self.assertTrue(issort_list([-5, -4, -3, -2, -1]))

    def test_edge_case_mixed_negative_positive(self):
        self.assertFalse(issort_list([-5, -4, 3, 2, 1]))

    def test_edge_case_mixed_negative_positive_descending(self):
        self.assertFalse(issort_list([-5, -4, 3, 2, 1]))

    def test_edge_case_mixed_negative_positive_ascending(self):
        self.assertFalse(issort_list([-5, -4, 3, 2, 1]))

    def test_edge_case_mixed_positive_negative(self):
        self.assertFalse(issort_list([5, 4, -3, -2, -1]))

    def test_edge_case_mixed_positive_negative_descending(self):
        self.assertFalse(issort_list([5, 4, -3, -2, -1]))

    def test_edge_case_mixed_positive_negative_ascending(self):
        self.assertFalse(issort_list([5, 4, -3, -2, -1]))

    def test_edge_case_mixed_positive(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))

    def test_edge_case_mixed_positive_descending(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))

    def test_edge_case_mixed_positive_ascending(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))

    def test_edge_case_mixed_negative(self):
        self.assertFalse(issort_list([-5, -4, -3, -2, -1]))

    def test_edge_case_mixed_negative_descending(self):
        self.assertFalse(issort_list([-5, -4, -3, -2, -1]))

    def test_edge_case_mixed_negative_ascending(self):
        self.assertFalse(issort_list([-5, -4, -3, -2, -1]))
