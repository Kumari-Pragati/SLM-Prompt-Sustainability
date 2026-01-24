import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):
    def test_largest_subset(self):
        self.assertEqual(largest_subset([1, 2, 3, 4, 5], 5), 2)
        self.assertEqual(largest_subset([1, 2, 3, 4, 6, 12], 6), 3)
        self.assertEqual(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 24, 30], 15), 4)
        self.assertEqual(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 2)
        self.assertEqual(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 30), 2)
        self.assertEqual(largest_subset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], 50), 2)
