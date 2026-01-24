import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(largest_subset([1, 2, 3], 3), 2)
        self.assertEqual(largest_subset([2, 4, 8], 3), 3)

    def test_edge_conditions(self):
        self.assertEqual(largest_subset([], 0), 0)
        self.assertEqual(largest_subset([1], 1), 1)
        self.assertEqual(largest_subset([1, 2, 3, 4, 5], 5), 4)

    def test_complex_cases(self):
        self.assertEqual(largest_subset([10, 20, 5, 30, 40], 5), 3)
        self.assertEqual(largest_subset([1, 1, 1, 1], 4), 4)
        self.assertEqual(largest_subset([10, 20, 15, 30, 5], 5), 3)
