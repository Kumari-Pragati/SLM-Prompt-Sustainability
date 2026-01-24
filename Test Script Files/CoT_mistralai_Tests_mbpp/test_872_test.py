import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_empty_lists(self):
        self.assertTrue(check_subset([], []))

    def test_single_element_lists(self):
        self.assertTrue(check_subset([1], [1]))
        self.assertFalse(check_subset([1], []))
        self.assertFalse(check_subset([], [1]))

    def test_identical_lists(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))

    def test_lists_with_duplicates(self):
        self.assertTrue(check_subset([1, 1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset([1, 2, 3, 3], [1, 2, 3]))

    def test_lists_in_reverse_order(self):
        self.assertTrue(check_subset([1, 2, 3], [3, 2, 1]))

    def test_lists_with_extra_elements(self):
        self.assertFalse(check_subset([1, 2, 3], [1, 2, 3, 4]))
        self.assertFalse(check_subset([1, 2, 3], [1, 2, 3, 1]))

    def test_lists_with_non_matching_elements(self):
        self.assertFalse(check_subset([1, 2, 3], [4, 5, 6]))
        self.assertFalse(check_subset([1, 2, "a"], [1, 2, "b"]))

    def test_lists_with_non_iterable_input(self):
        self.assertRaises(TypeError, check_subset, [1, 2, 3], 4)
        self.assertRaises(TypeError, check_subset, 4, [1, 2, 3])
