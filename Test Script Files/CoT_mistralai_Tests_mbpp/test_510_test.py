import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(no_of_subsequences([], 1), 1)

    def test_single_element_array(self):
        for k in range(1, 6):
            self.assertEqual(no_of_subsequences([k], k), 1)

    def test_increasing_array(self):
        arr = list(range(1, 6))
        self.assertEqual(no_of_subsequences(arr, 5), len(arr))

    def test_decreasing_array(self):
        arr = list(range(5, 0, -1))
        self.assertEqual(no_of_subsequences(arr, 5), len(arr))

    def test_array_with_duplicates(self):
        arr = [1, 1, 2, 3, 4]
        self.assertEqual(no_of_subsequences(arr, 5), 11)

    def test_array_with_zero(self):
        arr = [0, 1, 2, 3, 4]
        self.assertEqual(no_of_subsequences(arr, 5), 12)

    def test_array_with_negative_numbers(self):
        arr = [-1, -2, 0, 1, 2]
        self.assertEqual(no_of_subsequences(arr, 2), 7)

    def test_array_with_large_numbers(self):
        arr = list(range(100000))
        self.assertEqual(no_of_subsequences(arr, 100000), 1)

    def test_array_with_large_k(self):
        arr = [1, 2, 3]
        self.assertEqual(no_of_subsequences(arr, 1000000), 3)

    def test_invalid_input_empty_k(self):
        with self.assertRaises(ValueError):
            no_of_subsequences([1, 2, 3], 0)

    def test_invalid_input_negative_arr(self):
        with self.assertRaises(ValueError):
            no_of_subsequences([-1, -2, -3], 1)
