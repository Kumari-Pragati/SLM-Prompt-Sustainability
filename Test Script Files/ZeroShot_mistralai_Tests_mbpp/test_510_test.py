import unittest
from mbpp_510_code import no_of_subsequences

class TestNoOfSubsequences(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(no_of_subsequences([], 1), 1)

    def test_single_element_array(self):
        for k in range(1, 6):
            self.assertEqual(no_of_subsequences([k], k), 1)

    def test_simple_array(self):
        arr = [1, 2, 3, 4]
        for k in range(1, 6):
            self.assertEqual(no_of_subsequences(arr, k), sum([1 for i in range(1, len(arr) + 1) if arr[i - 1] <= k and arr[i - 1] > 0]))

    def test_complex_array(self):
        arr = [5, 3, 4, 8, 9, 7, 2, 1]
        for k in range(1, 9):
            self.assertEqual(no_of_subsequences(arr, k), sum([1 for i in range(1, len(arr) + 1) if arr[i - 1] <= k and arr[i - 1] > 0]))
