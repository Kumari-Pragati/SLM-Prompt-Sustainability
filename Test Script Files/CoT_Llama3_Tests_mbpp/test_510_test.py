import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case_k_zero(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5], 0), 0)

    def test_edge_case_n_zero(self):
        self.assertEqual(no_of_subsequences([], 5), 0)

    def test_edge_case_k_equal_n(self):
        self.assertEqual(no_of_subsequences([1, 2, 3, 4, 5], 5), 5)

    def test_invalid_input_negative_k(self):
        with self.assertRaises(ValueError):
            no_of_subsequences([1, 2, 3, 4, 5], -1)

    def test_invalid_input_negative_n(self):
        with self.assertRaises(ValueError):
            no_of_subsequences([-1, 2, 3, 4, 5], 5)
