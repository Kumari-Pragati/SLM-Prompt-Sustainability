import unittest
from mbpp_696_code import zip_list

class TestZipList(unittest.TestCase):

    def test_typical_case(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        expected_output = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(zip_list(list1, list2), expected_output)

    def test_empty_lists(self):
        list1 = []
        list2 = []
        expected_output = []
        self.assertEqual(zip_list(list1, list2), expected_output)

    def test_unequal_length_lists(self):
        list1 = [1, 2, 3]
        list2 = [4, 5]
        expected_output = [[1, 4], [2, 5]]
        self.assertEqual(zip_list(list1, list2), expected_output)

    def test_single_element_lists(self):
        list1 = [1]
        list2 = [2]
        expected_output = [[1, 2]]
        self.assertEqual(zip_list(list1, list2), expected_output)

    def test_negative_numbers(self):
        list1 = [-1, -2, -3]
        list2 = [-4, -5, -6]
        expected_output = [[-1, -4], [-2, -5], [-3, -6]]
        self.assertEqual(zip_list(list1, list2), expected_output)

    def test_zeroes(self):
        list1 = [0, 0, 0]
        list2 = [0, 0, 0]
        expected_output = [[0, 0], [0, 0], [0, 0]]
        self.assertEqual(zip_list(list1, list2), expected_output)
