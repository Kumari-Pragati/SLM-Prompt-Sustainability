import unittest
from mbpp_620_code import largest_subset

class TestLargestSubset(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(largest_subset([10, 5, 20, 15], 4), 4)

    def test_edge_case(self):
        self.assertEqual(largest_subset([], 0), 0)

    def test_boundary_case(self):
        self.assertEqual(largest_subset([1], 1), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            largest_subset("10, 5, 20, 15", 4)

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            largest_subset([10, 5, 20, 15], "4")
