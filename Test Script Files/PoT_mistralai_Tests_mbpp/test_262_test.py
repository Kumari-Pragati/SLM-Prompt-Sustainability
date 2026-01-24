import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 2), ([1, 2], [3, 4, 5]))
        self.assertEqual(split_two_parts([0, 0, 0, 0, 0], 4), ([0, 0, 0, 0], []))
        self.assertEqual(split_two_parts(['a', 'b', 'c', 'd', 'e'], 3), (['a', 'b', 'c'], ['d', 'e']))

    def test_edge_case_empty_list(self):
        self.assertEqual(split_two_parts([], 1), ([], []))

    def test_edge_case_single_element(self):
        self.assertEqual(split_two_parts([1], 0), ([], [1]))
        self.assertEqual(split_two_parts([1], 1), ([], []))

    def test_edge_case_single_element_negative(self):
        self.assertEqual(split_two_parts([1], -1), ([], [1]))
        self.assertEqual(split_two_parts([1], -2), ([], []))

    def test_edge_case_list_length_equal_to_split_index(self):
        self.assertEqual(split_two_parts([1, 2], 1), ([1], [2]))
        self.assertEqual(split_two_parts(['a', 'b'], 1), (['a'], ['b']))

    def test_corner_case_negative_index(self):
        self.assertEqual(split_two_parts([1, 2, 3], -1), ([1, 2, 3], []))
        self.assertEqual(split_two_parts(['a', 'b', 'c'], -1), (['a', 'b', 'c'], []))
