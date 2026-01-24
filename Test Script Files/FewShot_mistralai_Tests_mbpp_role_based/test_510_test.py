import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 3), 4)

    def test_edge_case_empty_array(self):
        self.assertEqual(no_of_subsequences([], 1), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(no_of_subsequences([1], 1), 1)

    def test_edge_case_k_greater_than_array_length(self):
        self.assertEqual(no_of_subsequences([1, 2], 3), 0)

    def test_edge_case_k_equal_to_array_length(self):
        self.assertEqual(no_of_subsequences([1, 2], 2), 3)

    def test_edge_case_k_less_than_1(self):
        self.assertEqual(no_of_subsequences([1, 2], 0), 0)

    def test_negative_elements(self):
        self.assertEqual(no_of_subsequences([-1, 2], 1), 1)

    def test_zero_elements(self):
        self.assertEqual(no_of_subsequences([0], 1), 1)
