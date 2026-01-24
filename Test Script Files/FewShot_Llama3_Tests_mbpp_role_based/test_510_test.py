import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        k = 3
        self.assertEqual(no_of_subsequences(arr, k), 7)

    def test_edge_case_k_zero(self):
        arr = [1, 2, 3, 4, 5]
        k = 0
        self.assertEqual(no_of_subsequences(arr, k), 1)

    def test_edge_case_n_zero(self):
        arr = []
        k = 3
        self.assertEqual(no_of_subsequences(arr, k), 0)

    def test_edge_case_k_greater_than_n(self):
        arr = [1, 2, 3, 4, 5]
        k = 10
        self.assertEqual(no_of_subsequences(arr, k), 5)

    def test_invalid_input_non_integer_k(self):
        arr = [1, 2, 3, 4, 5]
        k = 'three'
        with self.assertRaises(TypeError):
            no_of_subsequences(arr, k)

    def test_invalid_input_non_list_arr(self):
        arr = 'not a list'
        k = 3
        with self.assertRaises(TypeError):
            no_of_subsequences(arr, k)
