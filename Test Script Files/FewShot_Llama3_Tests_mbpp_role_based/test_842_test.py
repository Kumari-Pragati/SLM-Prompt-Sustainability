import unittest
from mbpp_842_code import get_odd_occurence

class TestGetOddOccurrence(unittest.TestCase):
    def test_single_element_array(self):
        arr = [1]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), 1)

    def test_multiple_elements_array(self):
        arr = [1, 2, 3, 4, 5]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), 1)

    def test_array_with_no_odd_occurrence(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), -1)

    def test_array_with_single_odd_occurrence(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), 5)

    def test_array_with_multiple_odd_occurrences(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5]
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), 5)

    def test_empty_array(self):
        arr = []
        arr_size = len(arr)
        self.assertEqual(get_odd_occurence(arr, arr_size), -1)
