import unittest
from mbpp_567_code import issort_list

class TestIsSortList(unittest.TestCase):

    def test_sorted_list(self):
        self.assertTrue(issort_list([1, 2, 3, 4, 5]))

    def test_unsorted_list(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))

    def test_empty_list(self):
        self.assertTrue(issort_list([]))

    def test_single_element_list(self):
        self.assertTrue(issort_list([1]))

    def test_duplicate_elements(self):
        self.assertTrue(issort_list([1, 2, 2, 3]))
