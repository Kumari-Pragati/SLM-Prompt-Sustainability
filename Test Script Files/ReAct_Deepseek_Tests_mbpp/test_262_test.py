import unittest
from mbpp_262_code import split_two_parts

class TestSplitTwoParts(unittest.TestCase):

    def test_typical_case(self):
        list1 = [1, 2, 3, 4, 5]
        L = 3
        expected_output = ([1, 2, 3], [4, 5])
        self.assertEqual(split_two_parts(list1, L), expected_output)

    def test_empty_list(self):
        list1 = []
        L = 3
        expected_output = ([], [])
        self.assertEqual(split_two_parts(list1, L), expected_output)

    def test_L_greater_than_list_length(self):
        list1 = [1, 2, 3]
        L = 5
        expected_output = ([1, 2, 3], [])
        self.assertEqual(split_two_parts(list1, L), expected_output)

    def test_L_equals_zero(self):
        list1 = [1, 2, 3]
        L = 0
        expected_output = ([], [1, 2, 3])
        self.assertEqual(split_two_parts(list1, L), expected_output)

    def test_negative_L(self):
        list1 = [1, 2, 3]
        L = -1
        with self.assertRaises(IndexError):
            split_two_parts(list1, L)
