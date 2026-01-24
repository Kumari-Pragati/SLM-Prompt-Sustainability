import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 3, 4, 9, 10, 11, 12, 17]
        n = len(arr)
        k = 4
        self.assertEqual(removals(arr, n, k), 2)

    def test_edge_case_k_zero(self):
        arr = [1, 3, 4, 9, 10, 11, 12, 17]
        n = len(arr)
        k = 0
        self.assertEqual(removals(arr, n, k), n-1)

    def test_boundary_case_k_large(self):
        arr = [1, 3, 4, 9, 10, 11, 12, 17]
        n = len(arr)
        k = 15
        self.assertEqual(removals(arr, n, k), 1)

    def test_invalid_input_negative_k(self):
        arr = [1, 3, 4, 9, 10, 11, 12, 17]
        n = len(arr)
        k = -1
        with self.assertRaises(Exception):
            removals(arr, n, k)

    def test_invalid_input_empty_array(self):
        arr = []
        n = 0
        k = 1
        with self.assertRaises(Exception):
            removals(arr, n, k)
