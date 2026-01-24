import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurence(unittest.TestCase):

    def test_typical_case(self):
        arr = [20, 10, 20, 30, 10, 10]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), 30)

    def test_edge_case_single_element(self):
        arr = [5]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), 5)

    def test_edge_case_all_elements_same(self):
        arr = [2, 2, 2, 2, 2]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), 2)

    def test_edge_case_no_odd_occurrence(self):
        arr = [1, 2, 3, 4, 5]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), -1)

    def test_edge_case_empty_array(self):
        arr = []
        arr_size = 0
        self.assertEqual(get_odd_occurence(arr, arr_size), -1)
