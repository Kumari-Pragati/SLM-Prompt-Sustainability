import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_binary_search_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(binary_search(arr, 0, len(arr) - 1, 5), 4)

    def test_binary_search_not_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(binary_search(arr, 0, len(arr) - 1, 0), -1)

    def test_binary_search_empty_list(self):
        arr = []
        self.assertEqual(binary_search(arr, 0, len(arr) - 1, 5), -1)

    def test_binary_search_single_element(self):
        arr = [5]
        self.assertEqual(binary_search(arr, 0, len(arr) - 1, 5), 0)

    def test_binary_search_negative_number(self):
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(binary_search(arr, 0, len(arr) - 1, -1), 0)

    def test_binary_search_out_of_range_value(self):
        arr = [1, 2, 3, 4, 5]
        self.assertRaises(ValueError, binary_search, arr, 0, len(arr) - 1, 10)
