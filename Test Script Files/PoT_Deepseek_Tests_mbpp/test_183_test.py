import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 7, 5, 9, 2, 12, 3, 2]
        n = len(arr)
        k = 2
        self.assertEqual(count_pairs(arr, n, k), 3)

    def test_edge_case_k_zero(self):
        arr = [1, 7, 5, 9, 2, 12, 3, 2]
        n = len(arr)
        k = 0
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_boundary_case_k_negative(self):
        arr = [1, 7, 5, 9, 2, 12, 3, 2]
        n = len(arr)
        k = -1
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_corner_case_single_element(self):
        arr = [1]
        n = len(arr)
        k = 2
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_corner_case_k_large(self):
        arr = [1, 7, 5, 9, 2, 12, 3, 2]
        n = len(arr)
        k = 15
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_invalid_input_negative_index(self):
        arr = [1, 7, 5, 9, 2, 12, 3, 2]
        n = -1
        k = 2
        with self.assertRaises(Exception):
            count_pairs(arr, n, k)

    def test_invalid_input_negative_element(self):
        arr = [-1, 7, 5, 9, 2, 12, 3, 2]
        n = len(arr)
        k = 2
        self.assertEqual(count_pairs(arr, n, k), 0)
