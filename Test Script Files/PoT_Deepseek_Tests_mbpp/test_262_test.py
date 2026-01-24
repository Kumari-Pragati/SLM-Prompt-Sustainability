import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 3), ([1, 2, 3], [4, 5]))

    def test_edge_case_L_equals_zero(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 0), ([], [1, 2, 3, 4, 5]))

    def test_boundary_case_L_equals_length_of_list(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 5), ([1, 2, 3, 4, 5], []))

    def test_corner_case_L_greater_than_length_of_list(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 6), ([1, 2, 3, 4, 5], []))

    def test_invalid_input_L_negative(self):
        with self.assertRaises(IndexError):
            split_two_parts([1, 2, 3, 4, 5], -1)

    def test_invalid_input_L_not_integer(self):
        with self.assertRaises(TypeError):
            split_two_parts([1, 2, 3, 4, 5], 'a')
