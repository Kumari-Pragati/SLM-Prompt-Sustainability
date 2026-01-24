import unittest
from mbpp_481_code import is_subset_sum

class TestIsSubsetSum(unittest.TestCase):
    def test_typical_case(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = 9
        self.assertTrue(is_subset_sum(set, n, sum))

    def test_boundary_condition(self):
        set = [0]
        n = len(set)
        sum = 0
        self.assertTrue(is_subset_sum(set, n, sum))

    def test_edge_condition(self):
        set = []
        n = len(set)
        sum = 10
        self.assertFalse(is_subset_sum(set, n, sum))

    def test_invalid_input(self):
        set = [3, 34, 4, 12, 5, 2]
        n = len(set)
        sum = 'invalid'
        with self.assertRaises(TypeError):
            is_subset_sum(set, n, sum)
