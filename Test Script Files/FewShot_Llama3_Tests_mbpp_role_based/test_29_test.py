import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):
    def test_single_odd_occurrence(self):
        arr = [1, 2, 3, 4, 5]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 1)

    def test_multiple_odd_occurrences(self):
        arr = [1, 2, 3, 4, 5, 1, 3]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 1)

    def test_no_odd_occurrences(self):
        arr = [2, 4, 6, 8, 10]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), -1)

    def test_empty_array(self):
        arr = []
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), -1)

    def test_single_element_array(self):
        arr = [1]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 1)

    def test_all_elements_same(self):
        arr = [1, 1, 1, 1, 1]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 1)
