import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 2), ([1, 2], [3, 4, 5]))

    def test_edge_case_empty_list(self):
        self.assertEqual(split_two_parts([], 1), ([], []))

    def test_edge_case_single_element(self):
        self.assertEqual(split_two_parts([1], 0), ([], [1]))
        self.assertEqual(split_two_parts([1], 1), ([], [1]))

    def test_edge_case_one_part_larger(self):
        self.assertEqual(split_two_parts([1, 2, 3], 2), ([1, 2], [3]))
        self.assertEqual(split_two_parts([1, 2, 3], 3), ([1, 2, 3], []))

    def test_edge_case_negative_index(self):
        self.assertRaises(IndexError, lambda: split_two_parts([1, 2, 3], -1))
        self.assertRaises(IndexError, lambda: split_two_parts([1, 2, 3], -2))
