import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3]
        k = 4
        self.assertEqual(no_of_subsequences(arr, k), 4)

    def test_edge_case_k_zero(self):
        arr = [1, 2, 3]
        k = 0
        self.assertEqual(no_of_subsequences(arr, k), 0)

    def test_edge_case_empty_array(self):
        arr = []
        k = 4
        self.assertEqual(no_of_subsequences(arr, k), 0)

    def test_edge_case_negative_elements(self):
        arr = [1, -2, 3]
        k = 4
        self.assertEqual(no_of_subsequences(arr, k), 3)

    def test_edge_case_zero_elements(self):
        arr = [0, 0, 0]
        k = 4
        self.assertEqual(no_of_subsequences(arr, k), 1)

    def test_invalid_input_negative_k(self):
        arr = [1, 2, 3]
        k = -4
        with self.assertRaises(Exception):
            no_of_subsequences(arr, k)

    def test_invalid_input_negative_elements_in_array(self):
        arr = [-1, -2, -3]
        k = 4
        with self.assertRaises(Exception):
            no_of_subsequences(arr, k)
