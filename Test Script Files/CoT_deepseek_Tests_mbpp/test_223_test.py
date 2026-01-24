import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_binary_search_exists(self):
        self.assertIsNotNone(binary_search)

    def test_binary_search_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        x = 4
        result = binary_search(arr, 0, len(arr) - 1, x)
        self.assertEqual(result, 3)

    def test_binary_search_edge_case_not_found(self):
        arr = [1, 2, 3, 4, 5]
        x = 6
        result = binary_search(arr, 0, len(arr) - 1, x)
        self.assertEqual(result, -1)

    def test_binary_search_edge_case_single_element(self):
        arr = [5]
        x = 5
        result = binary_search(arr, 0, len(arr) - 1, x)
        self.assertEqual(result, 0)

    def test_binary_search_edge_case_empty_array(self):
        arr = []
        x = 5
        result = binary_search(arr, 0, len(arr) - 1, x)
        self.assertEqual(result, -1)
