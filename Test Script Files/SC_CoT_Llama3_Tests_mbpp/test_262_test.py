import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):

    def test_typical_input(self):
        list1 = [1, 2, 3, 4, 5]
        L = 3
        result = split_two_parts(list1, L)
        self.assertEqual(result, ([1, 2, 3], [4, 5]))

    def test_edge_case_L_zero(self):
        list1 = [1, 2, 3, 4, 5]
        L = 0
        result = split_two_parts(list1, L)
        self.assertEqual(result, ([], [1, 2, 3, 4, 5]))

    def test_edge_case_L_equal_to_length(self):
        list1 = [1, 2, 3, 4, 5]
        L = 5
        result = split_two_parts(list1, L)
        self.assertEqual(result, ([1, 2, 3, 4, 5], []))

    def test_edge_case_L_greater_than_length(self):
        list1 = [1, 2, 3, 4, 5]
        L = 10
        result = split_two_parts(list1, L)
        self.assertEqual(result, ([1, 2, 3, 4, 5], []))

    def test_invalid_input_non_integer(self):
        list1 = [1, 2, 3, 4, 5]
        L = 'a'
        with self.assertRaises(TypeError):
            split_two_parts(list1, L)

    def test_invalid_input_negative(self):
        list1 = [1, 2, 3, 4, 5]
        L = -1
        with self.assertRaises(TypeError):
            split_two_parts(list1, L)
