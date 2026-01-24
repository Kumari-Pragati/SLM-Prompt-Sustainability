import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))
        self.assertFalse(check_subset([1, 2, 3], [1, 2, 4]))

    def test_empty_lists(self):
        self.assertTrue(check_subset([], []))
        self.assertTrue(check_subset([1, 2, 3], []))
        self.assertFalse(check_subset([], [1, 2, 3]))

    def test_single_element_lists(self):
        self.assertTrue(check_subset([1], [1]))
        self.assertFalse(check_subset([1], [2]))

    def test_duplicates(self):
        self.assertTrue(check_subset([1, 2, 2], [1, 2]))
        self.assertFalse(check_subset([1, 2, 2], [1, 2, 2, 2]))

    def test_edge_cases(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3, 4, 5]))
        self.assertFalse(check_subset([1, 2, 3], [4, 5, 6]))
