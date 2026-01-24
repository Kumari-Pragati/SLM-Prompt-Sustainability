import unittest
from mbpp_567_code import issort_list

class TestIssortList(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertTrue(issort_list([1, 2, 3, 4, 5]))

    def test_empty_input(self):
        self.assertFalse(issort_list([]))

    def test_single_element_input(self):
        self.assertTrue(issort_list([1]))

    def test_reverse_sorted_input(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))

    def test_already_sorted_input(self):
        self.assertTrue(issort_list([1, 2, 3, 4, 5]))

    def test_unsorted_input(self):
        self.assertFalse(issort_list([3, 1, 4, 1, 5, 9, 2, 6]))

    def test_duplicates_input(self):
        self.assertTrue(issort_list([1, 2, 2, 3, 3, 4, 5]))
