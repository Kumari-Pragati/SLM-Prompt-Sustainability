import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(no_of_subsequences([], 1), 0)

    def test_single_element_array(self):
        for k in range(1, 6):
            self.assertEqual(no_of_subsequences([1], k), 1)

    def test_increasing_array(self):
        arr = list(range(1, 6))
        for k in range(1, len(arr) + 1):
            self.assertEqual(no_of_subsequences(arr, k), 1)

    def test_decreasing_array(self):
        arr = list(range(5, 0, -1))
        for k in range(1, len(arr) + 1):
            self.assertEqual(no_of_subsequences(arr, k), 1)

    def test_mixed_array(self):
        arr = [5, 3, 4, 1, 2]
        for k in range(1, len(arr) + 1):
            self.assertEqual(no_of_subsequences(arr, k), 5)

    def test_zero_element(self):
        self.assertEqual(no_of_subsequences([0], 1), 1)

    def test_negative_element(self):
        with self.assertRaises(ValueError):
            no_of_subsequences([-1], 1)

    def test_k_greater_than_array_length(self):
        with self.assertRaises(ValueError):
            no_of_subsequences([1, 2, 3], 5)

    def test_k_less_than_one(self):
        with self.assertRaises(ValueError):
            no_of_subsequences([1, 2, 3], 0)
