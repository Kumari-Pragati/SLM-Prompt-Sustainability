import unittest
from mbpp_872_code import check_subset

class TestCheckSubset(unittest.TestCase):

    def test_simple_cases(self):
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3]))
        self.assertTrue(check_subset([], []))

    def test_edge_conditions(self):
        self.assertTrue(check_subset([1, 2, 3], []))
        self.assertFalse(check_subset([], [1, 2, 3]))

    def test_complex_cases(self):
        self.assertFalse(check_subset([1, 2, 3], [4, 5, 6]))
        self.assertFalse(check_subset([1, 2, 3], [1, 2]))
        self.assertTrue(check_subset([1, 2, 3], [1, 2, 3, 4, 5]))
