import unittest
from mbpp_408_code import k_smallest_pairs

class TestKSmallestPairs(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(k_smallest_pairs([1, 7, 11], [2, 4, 6], 3), [[1, 2], [1, 4], [1, 6]])

    def test_edge_conditions(self):
        self.assertEqual(k_smallest_pairs([], [], 0), [])
        self.assertEqual(k_smallest_pairs([1], [2], 1), [[1, 2]])
        self.assertEqual(k_smallest_pairs([1, 2, 3], [4, 5, 6], 6), [[1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5]])

    def test_complex_cases(self):
        self.assertEqual(k_smallest_pairs([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 10), 
                         [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7]])
