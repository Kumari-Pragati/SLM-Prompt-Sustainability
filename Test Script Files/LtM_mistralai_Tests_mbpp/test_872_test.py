import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_simple_subset(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2]))
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset([1, 2], [1, 2, 3]))

    def test_edge_cases(self):
        self.assertFalse(check_subset([1, 2], []))
        self.assertFalse(check_subset([], [1, 2]))
        self.assertFalse(check_subset([1, 2], [3]))
        self.assertFalse(check_subset([3], [1, 2]))

    def test_complex_cases(self):
        self.assertTrue(check_subset([1, 2, 3], [2, 1, 3]))
        self.assertTrue(check_subset([1, 2, 3], [3, 2, 1]))
        self.assertFalse(check_subset([1, 2, 3], [4, 5, 6]))
        self.assertFalse(check_subset([4, 5, 6], [1, 2, 3]))
