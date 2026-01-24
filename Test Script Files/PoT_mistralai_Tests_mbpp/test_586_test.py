import unittest
from mbpp_586_code import split_Arr

class TestSplitArr(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 2, 3), [(4, 5), (1, 2)])
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 3, 3), [(4, 5), (1, 2, 3)])
        self.assertEqual(split_Arr([1, 2, 3, 4, 5], 4, 3), [(4, 5), (1, 2, 3)])

    def test_edge_case_small_k(self):
        self.assertEqual(split_Arr([1, 2, 3], 2, 1), [(2, 3), [1]])
        self.assertEqual(split_Arr([1, 2, 3], 3, 1), [(2, 3), [1]])

    def test_edge_case_large_k(self):
        self.assertEqual(split_Arr([1, 2, 3], 2, 4), [(2, 3), [1]])
        self.assertEqual(split_Arr([1, 2, 3], 3, 4), [(2, 3), [1]])

    def test_corner_case_empty_list(self):
        self.assertEqual(split_Arr([], 2, 1), [([], [])])

    def test_corner_case_single_element(self):
        self.assertEqual(split_Arr([1], 1, 1), [([1], [])])
