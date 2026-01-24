import unittest
from mbpp_108_code import merge_sorted_list

class TestMergeSortedList(unittest.TestCase):

    def test_typical_case(self):
        num1 = [1, 3, 5]
        num2 = [2, 4, 6]
        num3 = [0, 7, 8]
        expected_output = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(merge_sorted_list(num1, num2, num3), expected_output)

    def test_empty_lists(self):
        num1 = []
        num2 = []
        num3 = []
        expected_output = []
        self.assertEqual(merge_sorted_list(num1, num2, num3), expected_output)

    def test_single_element_lists(self):
        num1 = [1]
        num2 = [2]
        num3 = [3]
        expected_output = [1, 2, 3]
        self.assertEqual(merge_sorted_list(num1, num2, num3), expected_output)

    def test_duplicate_elements(self):
        num1 = [1, 1, 2, 3]
        num2 = [1, 2, 2, 3]
        num3 = [1, 1, 2, 3]
        expected_output = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
        self.assertEqual(merge_sorted_list(num1, num2, num3), expected_output)

    def test_negative_numbers(self):
        num1 = [-3, -1, 1]
        num2 = [-2, 0, 2]
        num3 = [-3, -1, 1]
        expected_output = [-3, -3, -2, -1, -1, 0, 1, 1, 2, 2]
        self.assertEqual(merge_sorted_list(num1, num2, num3), expected_output)
