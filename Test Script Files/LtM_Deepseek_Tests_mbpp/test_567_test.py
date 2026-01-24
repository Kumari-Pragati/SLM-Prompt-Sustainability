import unittest
from mbpp_567_code import issort_list

class TestISSortList(unittest.TestCase):

    def test_simple_sorted_list(self):
        self.assertTrue(issort_list([1, 2, 3, 4, 5]))

    def test_simple_unsorted_list(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))

    def test_empty_list(self):
        self.assertTrue(issort_list([]))

    def test_single_element_list(self):
        self.assertTrue(issort_list([1]))

    def test_duplicate_elements_list(self):
        self.assertTrue(issort_list([1, 1, 2, 3]))

    def test_negative_numbers_sorted_list(self):
        self.assertTrue(issort_list([-5, -4, -3, -2, -1]))

    def test_negative_numbers_unsorted_list(self):
        self.assertFalse(issort_list([-1, -2, -3, -4, -5]))

    def test_mixed_positive_negative_sorted_list(self):
        self.assertFalse(issort_list([-1, 1, -2, 2, -3, 3]))

    def test_mixed_positive_negative_unsorted_list(self):
        self.assertFalse(issort_list([1, -1, 2, -2, 3, -3]))
