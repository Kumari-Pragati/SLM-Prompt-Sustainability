import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 3), ([1, 2, 3], [4, 5]))

    def test_edge_case_L_zero(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 0), ([], [1, 2, 3, 4, 5]))

    def test_edge_case_L_list_length(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 5), ([1, 2, 3, 4, 5], []))

    def test_edge_case_L_greater_than_list_length(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 10), ([1, 2, 3, 4, 5], []))

    def test_edge_case_L_negative(self):
        with self.assertRaises(ValueError):
            split_two_parts([1, 2, 3, 4, 5], -1)

    def test_edge_case_L_non_integer(self):
        with self.assertRaises(TypeError):
            split_two_parts([1, 2, 3, 4, 5], 'a')
