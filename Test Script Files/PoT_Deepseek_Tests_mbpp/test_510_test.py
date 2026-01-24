import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 3), 4)

    def test_edge_case_empty_array(self):
        self.assertEqual(no_of_subsequences([], 3), 0)

    def test_boundary_case_k_equals_zero(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 0), 1)

    def test_corner_case_k_greater_than_sum_of_elements(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 6), 8)

    def test_typical_case_with_duplicates(self):
        self.assertEqual(no_of_subsequences([1, 2, 2], 3), 4)

    def test_edge_case_negative_elements(self):
        self.assertEqual(no_of_subsequences([-1, -2, -3], 3), 1)

    def test_boundary_case_k_equals_one(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 1), 1)

    def test_corner_case_k_equals_one_and_array_contains_zero(self):
        self.assertEqual(no_of_subsequences([0, 1, 2], 1), 1)

    def test_invalid_case_negative_k(self):
        with self.assertRaises(Exception):
            no_of_subsequences([1, 2, 3], -1)
