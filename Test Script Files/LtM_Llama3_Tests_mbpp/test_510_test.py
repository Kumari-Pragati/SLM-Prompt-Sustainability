import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(no_of_subsequences([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(no_of_subsequences([1], 1), 1)

    def test_single_element_array_with_k_zero(self):
        self.assertEqual(no_of_subsequences([1], 0), 0)

    def test_array_with_k_greater_than_max(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 10), 3)

    def test_array_with_k_equal_to_max(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 3), 3)

    def test_array_with_k_less_than_min(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 0), 0)

    def test_array_with_k_equal_to_min(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 1), 1)

    def test_array_with_k_greater_than_max_and_k_greater_than_max(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 10), 3)

    def test_array_with_k_equal_to_max_and_k_equal_to_max(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 3), 3)

    def test_array_with_k_less_than_min_and_k_less_than_min(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 0), 0)

    def test_array_with_k_equal_to_min_and_k_equal_to_min(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 1), 1)
