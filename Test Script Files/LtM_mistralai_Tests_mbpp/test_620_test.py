import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(largest_subset([2, 3, 2, 1, 4], 5), 3)
        self.assertEqual(largest_subset([1, 1, 1], 3), 1)
        self.assertEqual(largest_subset([1, 2, 3, 4], 4), 4)

    def test_edge_cases(self):
        self.assertEqual(largest_subset([], 0), 0)
        self.assertEqual(largest_subset([1], 1), 1)
        self.assertEqual(largest_subset([1, 2, 1], 3), 2)
        self.assertEqual(largest_subset([2, 2, 2], 3), 3)
        self.assertEqual(largest_subset([1, 2, 2, 3, 1], 5), 3)

    def test_complex(self):
        self.assertEqual(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 10)
        self.assertEqual(largest_subset([1, 2, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2, 9, 2, 10], 18), 10)
        self.assertEqual(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20), 10)
