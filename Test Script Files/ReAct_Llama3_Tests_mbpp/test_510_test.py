import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(no_of_subsequences([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(no_of_subsequences([1], 1), 1)

    def test_multiple_elements_array(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 3), 3)

    def test_k_is_greater_than_array_length(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 10), 3)

    def test_k_is_zero(self):
        self.assertEqual(no_of_subsequences([1, 2, 3], 0), 0)

    def test_array_with_negative_elements(self):
        self.assertEqual(no_of_subsequences([-1, -2, -3], 3), 3)

    def test_array_with_zero(self):
        self.assertEqual(no_of_subsequences([0, 1, 2], 2), 2)

    def test_array_with_duplicates(self):
        self.assertEqual(no_of_subsequences([1, 1, 2, 2, 3], 3), 3)
