import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):
    def test_typical_use_case(self):
        a = [2, 3, 4, 6, 8, 12, 24]
        n = len(a)
        self.assertEqual(largest_subset(a, n), 4)

    def test_edge_case(self):
        a = [1, 2, 3, 4, 5, 6]
        n = len(a)
        self.assertEqual(largest_subset(a, n), 1)

    def test_boundary_case(self):
        a = [1, 2, 3, 4, 5, 6, 7]
        n = len(a)
        self.assertEqual(largest_subset(a, n), 2)

    def test_invalid_input(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(a) + 1
        with self.assertRaises(IndexError):
            largest_subset(a, n)
