import unittest
from mbpp_548_code import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]), 5)

    def test_single_element(self):
        self.assertEqual(longest_increasing_subsequence([5]), 1)

    def test_empty_list(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)

    def test_decreasing_sequence(self):
        self.assertEqual(longest_increasing_subsequence([30, 20, 10]), 1)

    def test_same_elements(self):
        self.assertEqual(longest_increasing_subsequence([1, 1, 1, 1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(longest_increasing_subsequence([-1, -2, -3, -4]), 1)

    def test_large_numbers(self):
        self.assertEqual(longest_increasing_subsequence([1000, 2000, 3000, 4000]), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            longest_increasing_subsequence("1,2,3,4")

        with self.assertRaises(TypeError):
            longest_increasing_subsequence(1234)

        with self.assertRaises(TypeError):
            longest_increasing_subsequence(None)
