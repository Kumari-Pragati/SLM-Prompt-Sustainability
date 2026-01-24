import unittest
from mbpp_31_code import defaultdict
import heapq

class TestFunc(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(func([[3, 1, 2, 4], [3, 4, 5, 6]], 3), [1, 2, 4])
        self.assertListEqual(func([[1, 2, 3], [4, 5, 6]], 2), [2, 3])
        self.assertListEqual(func([[1], [2], [3]], 1), [1])

    def test_edge_case_empty_list(self):
        self.assertListEqual(func([], 3), [])

    def test_edge_case_single_list(self):
        self.assertListEqual(func([[1]], 1), [1])

    def test_edge_case_single_element(self):
        self.assertListEqual(func([[1]], 3), [1])

    def test_edge_case_k_larger_than_nums_length(self):
        self.assertListEqual(func([[1]], 4), [1])

    def test_corner_case_duplicates(self):
        self.assertListEqual(func([[1, 1], [2, 2]], 2), [1, 2])

    def test_corner_case_negative_numbers(self):
        self.assertListEqual(func([[1, -1], [2, -2]], 2), [1, -1])
