import unittest
from mbpp_567_code import issort_list

class TestIssortList(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(issort_list([1, 2, 3, 4, 5]))

    def test_edge_case_descending(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))

    def test_edge_case_ascending(self):
        self.assertTrue(issort_list([1, 1, 1, 1, 1]))

    def test_edge_case_single_element(self):
        self.assertTrue(issort_list([1]))

    def test_edge_case_empty_list(self):
        self.assertTrue(issort_list([]))

    def test_edge_case_single_element_descending(self):
        self.assertFalse(issort_list([5]))

    def test_edge_case_single_element_ascending(self):
        self.assertTrue(issort_list([1]))

    def test_edge_case_two_elements_ascending(self):
        self.assertTrue(issort_list([1, 2]))

    def test_edge_case_two_elements_descending(self):
        self.assertFalse(issort_list([2, 1]))

    def test_edge_case_three_elements_ascending(self):
        self.assertTrue(issort_list([1, 2, 3]))

    def test_edge_case_three_elements_descending(self):
        self.assertFalse(issort_list([3, 2, 1]))
