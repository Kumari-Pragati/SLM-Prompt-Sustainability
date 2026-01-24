import unittest
from mbpp_548_code import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]), 5)

    def test_edge_case_single_element(self):
        self.assertEqual(longest_increasing_subsequence([1]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)

    def test_corner_case_decreasing_sequence(self):
        self.assertEqual(longest_increasing_subsequence([30, 20, 10]), 1)

    def test_corner_case_increasing_sequence(self):
        self.assertEqual(longest_increasing_subsequence([10, 20, 30]), 3)

    def test_corner_case_same_elements(self):
        self.assertEqual(longest_increasing_subsequence([10, 10, 10]), 1)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            longest_increasing_subsequence(['a', 'b', 'c'])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            longest_increasing_subsequence('12345')
