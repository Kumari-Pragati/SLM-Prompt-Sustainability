import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_majority_element_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        x = 5
        self.assertTrue(is_majority(arr, n, x))

    def test_majority_element_not_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        x = 11
        self.assertFalse(is_majority(arr, n, x))

    def test_binary_search_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        x = 5
        self.assertEqual(binary_search(arr, 0, n-1, x), 4)

    def test_binary_search_not_found(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        x = 11
        self.assertEqual(binary_search(arr, 0, n-1, x), -1)

    def test_binary_search_edge_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 1
        self.assertEqual(binary_search(arr, 0, n-1, x), 0)

    def test_binary_search_invalid_input(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = "string"
        with self.assertRaises(TypeError):
            binary_search(arr, 0, n-1, x)
