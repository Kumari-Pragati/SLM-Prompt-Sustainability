import unittest
from mbpp_183_code import count_pairs

class TestCountPairs(unittest.TestCase):

    def test_typical_input(self):
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
        k = 100
        self.assertEqual(count_pairs(arr, n, k), 2)

    def test_edge_case_n_one(self):
        arr = [1]
        n = len(arr)
        k = 1
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_edge_case_n_zero(self):
        arr = []
        n = len(arr)
        k = 1
        self.assertEqual(count_pairs(arr, n, k), 0)

    def test_invalid_input_non_integer_k(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        k = 'a'
        with self.assertRaises(TypeError):
            count_pairs(arr, n, k)

    def test_invalid_input_non_integer_n(self):
        arr = [1, 2, 3, 4, 5]
        n = 'a'
        k = 1
        with self.assertRaises(TypeError):
            count_pairs(arr, n, k)

    def test_invalid_input_non_list_arr(self):
        arr = 'a'
        n = len(arr)
        k = 1
        with self.assertRaises(TypeError):
            count_pairs(arr, n, k)
