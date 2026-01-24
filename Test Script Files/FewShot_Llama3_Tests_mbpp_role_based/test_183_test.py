import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 1
        self.assertEqual(count_pairs(arr, n, k), 2)

    def test_edge_case_k_zero(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 0
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_edge_case_k_large(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 10
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_invalid_input_arr_length_zero(self):
        arr = []
        n = len(arr)
        k = 1
        with self.assertRaises(IndexError):
            count_pairs(arr, n, k)

    def test_invalid_input_arr_length_negative(self):
        arr = [-1, -2, -3]
        n = len(arr)
        k = 1
        with self.assertRaises(IndexError):
            count_pairs(arr, n, k)
