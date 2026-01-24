import unittest
from mbpp_567_code import issort_list

class TestIssortList(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(issort_list([]))

    def test_single_element_list(self):
        self.assertTrue(issort_list([1]))

    def test_sorted_list(self):
        self.assertTrue(issort_list([1, 2, 3, 4, 5]))

    def test_unsorted_list(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))

    def test_list_with_duplicates(self):
        self.assertTrue(issort_list([1, 2, 2, 3, 3, 3, 4, 5]))

    def test_list_with_duplicates_and_unsorted(self):
        self.assertFalse(issort_list([5, 4, 3, 3, 2, 2, 1]))

    def test_list_with_duplicates_and_unsorted_edge(self):
        self.assertFalse(issort_list([5, 4, 3, 3, 2, 2, 1, 0]))
