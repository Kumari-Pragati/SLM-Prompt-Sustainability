import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_binary_search_typical(self):
        arr = [1, 3, 5, 7, 9]
        x = 7
        result = binary_search(arr, 0, len(arr) - 1, x)
        self.assertEqual(result, 3)

    def test_binary_search_edge(self):
        arr = [1, 3, 5, 7, 9]
        x = 10
        result = binary_search(arr, 0, len(arr) - 1, x)
        self.assertEqual(result, -1)

    def test_binary_search_empty(self):
        arr = []
        x = 7
        result = binary_search(arr, 0, len(arr) - 1, x)
        self.assertEqual(result, -1)

    def test_is_majority_typical(self):
        arr = [1, 3, 3, 5, 7, 7, 9]
        x = 7
        result = is_majority(arr, len(arr), x)
        self.assertTrue(result)

    def test_is_majority_edge(self):
        arr = [1, 3, 3, 5, 7, 7, 9]
        x = 10
        result = is_majority(arr, len(arr), x)
        self.assertFalse(result)

    def test_is_majority_empty(self):
        arr = []
        x = 7
        result = is_majority(arr, len(arr), x)
        self.assertFalse(result)
