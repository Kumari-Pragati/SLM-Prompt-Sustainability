import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset(['a', 'b', 'c'], ['a', 'b', 'c']))

    def test_empty_lists(self):
        self.assertTrue(check_subset([], []))
        self.assertTrue(check_subset([], [1, 2, 3]))
        self.assertTrue(check_subset(['a', 'b', 'c'], []))

    def test_subset_case(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))
        self.assertTrue(check_subset(['a', 'b', 'c'], ['a', 'b']))

    def test_non_subset_case(self):
        self.assertFalse(check_subset([1, 2, 3], [4, 5, 6]))
        self.assertFalse(check_subset(['a', 'b', 'c'], ['d', 'e', 'f']))

    def test_duplicate_elements(self):
        self.assertTrue(check_subset([1, 2, 2], [1, 2]))
        self.assertFalse(check_subset([1, 2, 2], [1, 2, 3]))
