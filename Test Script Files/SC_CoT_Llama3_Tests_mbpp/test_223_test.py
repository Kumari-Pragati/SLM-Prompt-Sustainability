import unittest
from mbpp_223_code import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_majority_found(self):
        arr = [1, 2, 3, 2, 3, 2, 1]
        n = len(arr)
        x = 2
        self.assertTrue(is_majority(arr, n, x))

    def test_majority_not_found(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        x = 6
        self.assertFalse(is_majority(arr, n, x))

    def test_majority_found_at_middle(self):
        arr = [1, 2, 3, 2, 3, 2, 1]
        n = len(arr)
        x = 2
        self.assertTrue(is_majority(arr, n, x))

    def test_majority_found_at_start(self):
        arr = [1, 2, 3, 2, 3, 2, 1]
        n = len(arr)
        x = 1
        self.assertTrue(is_majority(arr, n, x))

    def test_majority_found_at_end(self):
        arr = [1, 2, 3, 2, 3, 2, 1]
        n = len(arr)
        x = 1
        self.assertTrue(is_majority(arr, n, x))

    def test_majority_found_at_start_and_end(self):
        arr = [1, 2, 3, 2, 3, 2, 1]
        n = len(arr)
        x = 1
        self.assertTrue(is_majority(arr, n, x))

    def test_binary_search_edge_cases(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(binary_search(arr, 0, n-1, 1), 0)
        self.assertEqual(binary_search(arr, 0, n-1, 5), 4)
        self.assertEqual(binary_search(arr, 0, n-1, 6), -1)

    def test_binary_search_invalid_inputs(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(binary_search(arr, -1, n-1, 1), -1)
        self.assertEqual(binary_search(arr, 0, n, 1), -1)
        self.assertEqual(binary_search(arr, 0, n-1, 1), 0)
