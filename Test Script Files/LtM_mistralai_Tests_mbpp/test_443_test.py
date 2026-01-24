import unittest
from mbpp_443_code import largest_neg

class TestLargestNeg(unittest.TestCase):

    def test_simple_positive_list(self):
        self.assertEqual(largest_neg([]), float('-inf'))

    def test_simple_negative_list(self):
        self.assertEqual(largest_neg([-1, -2, -3]), -3)

    def test_simple_mixed_list(self):
        self.assertEqual(largest_neg([-1, 0, -2, 3]), -2)

    def test_edge_case_empty_list(self):
        self.assertEqual(largest_neg([float('-inf')]), float('-inf'))

    def test_edge_case_single_element(self):
        self.assertEqual(largest_neg([float('-inf')]), float('-inf'))
        self.assertEqual(largest_neg([-1]), -1)
        self.assertEqual(largest_neg([float('inf')]), float('-inf'))

    def test_edge_case_min_max_values(self):
        self.assertEqual(largest_neg([float('-inf'), -1, 0, 1, float('inf')]), float('-inf'))
