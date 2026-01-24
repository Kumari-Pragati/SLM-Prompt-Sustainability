import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(largest_subset([1, 3, 2, 1, 4, 2, 3], 7), 4)
        self.assertEqual(largest_subset([2, 3, 2, 1, 2, 3, 4], 7), 5)
        self.assertEqual(largest_subset([1, 1, 1, 1, 1], 5), 1)

    def test_edge_cases(self):
        self.assertEqual(largest_subset([], 0), 0)
        self.assertEqual(largest_subset([1], 1), 1)
        self.assertEqual(largest_subset([1, 1], 2), 2)
        self.assertEqual(largest_subset([1, 1, 1], 3), 3)

    def test_corner_cases(self):
        self.assertEqual(largest_subset([1, 1, 2, 1, 1], 5), 3)
        self.assertEqual(largest_subset([1, 2, 2, 1, 1], 5), 3)
        self.assertEqual(largest_subset([2, 2, 2, 2, 2], 5), 5)
        self.assertEqual(largest_subset([1, 2, 3, 4, 5], 5), 2)
        self.assertEqual(largest_subset([5, 4, 3, 2, 1], 5), 2)
