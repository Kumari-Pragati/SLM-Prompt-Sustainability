import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):

    def test_typical_case(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = 9
        self.assertTrue(is_subset_sum(set, n, sum))

    def test_boundary_case(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = 0
        self.assertTrue(is_subset_sum(set, n, sum))

    def test_edge_case(self):
        set = []
        n = 0
        sum = 10
        self.assertFalse(is_subset_sum(set, n, sum))

    def test_corner_case(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = 100
        self.assertFalse(is_subset_sum(set, n, sum))

    def test_invalid_input(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = -10
        with self.assertRaises(Exception):
            is_subset_sum(set, n, sum)
