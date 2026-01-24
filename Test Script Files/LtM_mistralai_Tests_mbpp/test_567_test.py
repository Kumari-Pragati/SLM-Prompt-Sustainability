import unittest
from mbpp_567_code import issort_list

class TestIssortList(unittest.TestCase):
    def test_simple_sorted(self):
        self.assertTrue(issort_list([1, 2, 3]))

    def test_simple_reverse(self):
        self.assertFalse(issort_list([3, 2, 1]))

    def test_simple_single_element(self):
        self.assertTrue(issort_list([1]))

    def test_simple_duplicates(self):
        self.assertTrue(issort_list([1, 1, 2, 3]))

    def test_edge_empty_list(self):
        self.assertFalse(issort_list([]))

    def test_edge_single_decreasing(self):
        self.assertFalse(issort_list([3, 2]))

    def test_edge_single_increasing(self):
        self.assertTrue(issort_list([1]))

    def test_edge_single_decreasing_then_increasing(self):
        self.assertFalse(issort_list([3, 2, 1]))

    def test_edge_single_increasing_then_decreasing(self):
        self.assertFalse(issort_list([1, 3]))

    def test_edge_duplicates_decreasing(self):
        self.assertFalse(issort_list([3, 3, 2]))

    def test_edge_duplicates_increasing(self):
        self.assertTrue(issort_list([1, 1, 2]))

    def test_edge_duplicates_mixed(self):
        self.assertFalse(issort_list([3, 1, 1, 2]))
