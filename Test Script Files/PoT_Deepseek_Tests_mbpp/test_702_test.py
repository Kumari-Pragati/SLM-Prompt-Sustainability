import unittest
from mbpp_702_code import removals

class TestRemovals(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 3, 4, 9, 10, 11, 12, 17]
        n = len(arr)
        k = 2
        self.assertEqual(removals(arr, n, k), 2)

    def test_edge_case_k_zero(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 0
        self.assertEqual(removals(arr, n, k), n-1)

    def test_boundary_case_k_large(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 100
        self.assertEqual(removals(arr, n, k), 0)

    def test_corner_case_duplicate_elements(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        k = 1
        self.assertEqual(removals(arr, n, k), 0)

    def test_corner_case_large_array(self):
        arr = list(range(1, 10001))
        n = len(arr)
        k = 100
        self.assertEqual(removals(arr, n, k), 1)
