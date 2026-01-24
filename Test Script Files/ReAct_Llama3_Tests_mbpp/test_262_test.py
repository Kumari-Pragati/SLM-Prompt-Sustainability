import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):

    def test_typical_case(self):
        list1 = [1, 2, 3, 4, 5]
        L = 3
        result1, result2 = split_two_parts(list1, L)
        self.assertEqual(result1, [1, 2, 3])
        self.assertEqual(result2, [4, 5])

    def test_edge_case_L_zero(self):
        list1 = [1, 2, 3, 4, 5]
        L = 0
        result1, result2 = split_two_parts(list1, L)
        self.assertEqual(result1, [])
        self.assertEqual(result2, [1, 2, 3, 4, 5])

    def test_edge_case_L_equal_to_list_length(self):
        list1 = [1, 2, 3, 4, 5]
        L = 5
        result1, result2 = split_two_parts(list1, L)
        self.assertEqual(result1, [1, 2, 3, 4, 5])
        self.assertEqual(result2, [])

    def test_edge_case_L_greater_than_list_length(self):
        list1 = [1, 2, 3, 4, 5]
        L = 10
        result1, result2 = split_two_parts(list1, L)
        self.assertEqual(result1, [1, 2, 3, 4, 5])
        self.assertEqual(result2, [])

    def test_error_case_non_integer_L(self):
        list1 = [1, 2, 3, 4, 5]
        L = 'a'
        with self.assertRaises(TypeError):
            split_two_parts(list1, L)

    def test_error_case_negative_L(self):
        list1 = [1, 2, 3, 4, 5]
        L = -1
        with self.assertRaises(TypeError):
            split_two_parts(list1, L)
