import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):

    def test_typical_inputs(self):
        num1 = [1, 3, 5]
        num2 = [2, 4, 6]
        num3 = [0, 7, 8]
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(merge_sorted_list(num1, num2, num3), expected)

    def test_edge_case_empty_list(self):
        num1 = []
        num2 = []
        num3 = []
        expected = []
        self.assertEqual(merge_sorted_list(num1, num2, num3), expected)

    def test_edge_case_single_list(self):
        num1 = [1, 3, 5]
        num2 = []
        num3 = []
        expected = [1, 3, 5]
        self.assertEqual(merge_sorted_list(num1, num2, num3), expected)

    def test_edge_case_two_empty_lists(self):
        num1 = []
        num2 = []
        num3 = [0, 7, 8]
        expected = [0, 7, 8]
        self.assertEqual(merge_sorted_list(num1, num2, num3), expected)

    def test_edge_case_two_single_lists(self):
        num1 = [1, 3, 5]
        num2 = [2, 4, 6]
        num3 = []
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(merge_sorted_list(num1, num2, num3), expected)

    def test_invalid_input_type(self):
        num1 = [1, 3, 5]
        num2 = "invalid"
        num3 = [0, 7, 8]
        with self.assertRaises(TypeError):
            merge_sorted_list(num1, num2, num3)

    def test_invalid_input_value(self):
        num1 = [1, 3, 5]
        num2 = [2, 4, 6]
        num3 = "invalid"
        with self.assertRaises(TypeError):
            merge_sorted_list(num1, num2, num3)
