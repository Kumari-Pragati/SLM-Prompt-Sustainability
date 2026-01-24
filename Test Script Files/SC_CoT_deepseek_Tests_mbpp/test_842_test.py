import unittest

from mbpp_842_code import get_odd_occurence

class TestGetOddOccurence(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 2, 1, 3, 1, 3, 2, 2]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), 1)

    def test_edge_case_single_element(self):
        arr = [1]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), 1)

    def test_edge_case_all_same_elements(self):
        arr = [1, 1, 1, 1, 1]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), 1)

    def test_edge_case_all_different_elements(self):
        arr = [1, 2, 3, 4, 5]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), -1)

    def test_corner_case_empty_array(self):
        arr = []
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), -1)

    def test_invalid_input_negative_number(self):
        arr = [-1, 2, 3, 2, 1, 3, 1, 3, 2, 2]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), -1)
