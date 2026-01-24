import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 7, 5, 9, 2, 12, 3]
        n = len(arr)
        k = 2
        self.assertEqual(count_pairs(arr, n, k), 2)

    def test_edge_case_k_zero(self):
        arr = [1, 7, 5, 9, 2, 12, 3]
        n = len(arr)
        k = 0
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_edge_case_single_element(self):
        arr = [1]
        n = len(arr)
        k = 2
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_edge_case_negative_k(self):
        arr = [1, 7, 5, 9, 2, 12, 3]
        n = len(arr)
        k = -2
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_edge_case_large_k(self):
        arr = [1, 7, 5, 9, 2, 12, 3]
        n = len(arr)
        k = 15
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_error_case_negative_elements(self):
        arr = [-1, 7, 5, 9, 2, 12, 3]
        n = len(arr)
        k = 2
        with self.assertRaises(Exception):
            count_pairs(arr, n, k)

    def test_error_case_non_integer_elements(self):
        arr = [1, 7, 5, 9, 2, 12, 3.5]
        n = len(arr)
        k = 2
        with self.assertRaises(Exception):
            count_pairs(arr, n, k)
