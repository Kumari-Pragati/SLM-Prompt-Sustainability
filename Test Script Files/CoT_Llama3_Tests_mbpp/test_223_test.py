import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_majority(self):
        arr = [1, 2, 3, 2, 3, 2, 1]
        n = len(arr)
        x = 2
        self.assertTrue(is_majority(arr, n, x))

    def test_not_majority(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 6
        self.assertFalse(is_majority(arr, n, x))

    def test_edge_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 5
        self.assertTrue(is_majority(arr, n, x))

    def test_invalid_input(self):
        arr = [1, 2, 3]
        n = 0
        x = 4
        with self.assertRaises(IndexError):
            is_majority(arr, n, x)

    def test_binary_search_edge_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 1
        self.assertEqual(binary_search(arr, 0, n-1, x), 0)

    def test_binary_search_edge_case2(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 5
        self.assertEqual(binary_search(arr, 0, n-1, x), n-1)

    def test_binary_search_edge_case3(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 3
        self.assertEqual(binary_search(arr, 0, n-1, x), 2)
