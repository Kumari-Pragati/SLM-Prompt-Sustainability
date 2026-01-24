import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):
    def test_typical(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset([1, 2, 3], [2, 1, 3]))
        self.assertTrue(check_subset([1, 2, 3], [3, 2, 1]))

    def test_edge(self):
        self.assertFalse(check_subset([1, 2, 3], [4, 2, 3]))
        self.assertFalse(check_subset([1, 2, 3], []))
        self.assertFalse(check_subset([], [1, 2, 3]))

    def test_corner(self):
        self.assertTrue(check_subset([], []))
        self.assertTrue(check_subset([1], [1]))
        self.assertFalse(check_subset([1], [2]))
