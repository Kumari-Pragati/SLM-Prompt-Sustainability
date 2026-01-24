import unittest
from mbpp_567_code import issort_list

class TestIssortList(unittest.TestCase):

    def test_sorted_list(self):
        self.assertTrue(issort_list([1, 2, 3, 4, 5]))

    def test_reverse_sorted_list(self):
        self.assertFalse(issort_list([5, 4, 3, 2, 1]))

    def test_single_element_list(self):
        self.assertTrue(issort_list([1]))

    def test_empty_list(self):
        self.assertRaises(ValueError, issort_list, [])

    def test_duplicates_increasing(self):
        self.assertTrue(issort_list([1, 1, 2, 3, 4]))

    def test_duplicates_decreasing(self):
        self.assertFalse(issort_list([4, 4, 3, 2, 1]))

    def test_duplicates_mixed(self):
        self.assertFalse(issort_list([1, 4, 1, 3, 4]))

    def test_negative_numbers(self):
        self.assertTrue(issort_list([-1, -2, -3]))

    def test_mixed_positive_and_negative_numbers(self):
        self.assertTrue(issort_list([-1, 0, 1]))
