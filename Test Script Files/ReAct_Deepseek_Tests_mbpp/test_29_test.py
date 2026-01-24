import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):

    def test_typical_case(self):
        arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 5)

    def test_single_element(self):
        arr = [1]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 1)

    def test_no_odd_occurrence(self):
        arr = [1, 1, 2, 2, 3, 3]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), -1)

    def test_empty_array(self):
        arr = []
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), -1)

    def test_negative_numbers(self):
        arr = [-1, -2, -1, -2, -3, -3]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), -1)

    def test_large_numbers(self):
        arr = [1000, 2000, 1000, 2000, 3000, 3000]
        arr_size = len(arr)
        self.assertEqual(get_Odd_Occurrence(arr, arr_size), 1000)
