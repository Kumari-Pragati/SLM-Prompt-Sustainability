import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 4, 9, 10, 11, 12, 17]
        n = len(arr)
        k = 4
        self.assertEqual(removals(arr, n, k), 2)

    def test_edge_case_with_single_element(self):
        arr = [5]
        n = len(arr)
        k = 10
        self.assertEqual(removals(arr, n, k), 0)

    def test_edge_case_with_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 1
        self.assertEqual(removals(arr, n, k), 1)

    def test_edge_case_with_large_k(self):
        arr = [1, 3, 4, 9, 10, 11, 12, 17]
        n = len(arr)
        k = 20
        self.assertEqual(removals(arr, n, k), 0)

    def test_error_case_with_empty_array(self):
        arr = []
        n = 0
        k = 10
        with self.assertRaises(IndexError):
            removals(arr, n, k)
