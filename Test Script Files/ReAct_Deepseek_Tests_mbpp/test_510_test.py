import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3]
        k = 4
        self.assertEqual(no_of_subsequences(arr, k), 4)

    def test_typical_case_with_duplicates(self):
        arr = [1, 2, 2]
        k = 4
        self.assertEqual(no_of_subsequences(arr, k), 3)

    def test_edge_case_with_zero(self):
        arr = [0, 1, 2]
        k = 4
        self.assertEqual(no_of_subsequences(arr, k), 0)

    def test_edge_case_with_negative_numbers(self):
        arr = [-1, -2, -3]
        k = 4
        self.assertEqual(no_of_subsequences(arr, k), 0)

    def test_edge_case_with_large_numbers(self):
        arr = [100, 200, 300]
        k = 4
        self.assertEqual(no_of_subsequences(arr, k), 1)

    def test_error_case_with_empty_array(self):
        arr = []
        k = 4
        self.assertEqual(no_of_subsequences(arr, k), 0)
