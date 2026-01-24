import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):

    def test_typical_case(self):
        arr = [20, 10, 20, 30, 10, 10]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 30)

    def test_edge_case_single_element(self):
        arr = [5]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 5)

    def test_edge_case_all_same_elements(self):
        arr = [2, 2, 2, 2, 2]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 2)

    def test_edge_case_empty_array(self):
        arr = []
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), -1)

    def test_corner_case_multiple_odd_occurrences(self):
        arr = [10, 10, 20, 20, 30, 30, 40]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 40)

    def test_invalid_input_negative_numbers(self):
        arr = [-10, -10, -20, -20, -30, -30, -40]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), -1)
