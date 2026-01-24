import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 3), ([1, 2, 3], [4, 5]))

    def test_edge_case_empty_list(self):
        self.assertEqual(split_two_parts([], 3), ([], []))

    def test_edge_case_L_equals_zero(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 0), ([], [1, 2, 3, 4, 5]))

    def test_edge_case_L_equals_length_of_list(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 5), ([1, 2, 3, 4, 5], []))

    def test_boundary_case_L_greater_than_length_of_list(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5], 6), ([1, 2, 3, 4, 5], []))

    def test_complex_case_L_in_the_middle(self):
        self.assertEqual(split_two_parts([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7), ([1, 2, 3, 4, 5, 6, 7], [8, 9, 10]))
