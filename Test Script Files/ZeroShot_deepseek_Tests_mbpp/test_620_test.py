import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):

    def test_largest_subset(self):
        self.assertEqual(largest_subset([10, 5, 20, 15], 4), 4)
        self.assertEqual(largest_subset([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(largest_subset([10, 20, 30, 40, 50], 5), 5)
        self.assertEqual(largest_subset([1, 1, 1, 1, 1], 5), 5)
        self.assertEqual(largest_subset([10, 20, 15, 30, 5], 5), 4)
