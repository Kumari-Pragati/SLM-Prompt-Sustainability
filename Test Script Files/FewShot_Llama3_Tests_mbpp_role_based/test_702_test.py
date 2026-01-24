import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        k = 2
        self.assertEqual(removals(arr, n, k), 3)

    def test_edge_case_k_zero(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        k = 0
        self.assertEqual(removals(arr, n, k), n - 1)

    def test_edge_case_k_large(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        k = 100
        self.assertEqual(removals(arr, n, k), 1)

    def test_invalid_input_negative_k(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(arr)
        k = -1
        with self.assertRaises(ValueError):
            removals(arr, n, k)

    def test_invalid_input_empty_array(self):
        arr = []
        n = len(arr)
        k = 2
        with self.assertRaises(IndexError):
            removals(arr, n, k)
