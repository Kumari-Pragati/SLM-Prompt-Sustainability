import unittest
from mbpp_149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(longest_subseq_with_diff_one([], 0), 0)

    def test_single_element(self):
        for element in range(10):
            self.assertEqual(longest_subseq_with_diff_one([element], 1), 1)

    def test_consecutive_elements(self):
        for i in range(1, 10):
            self.assertEqual(longest_subseq_with_diff_one(list(range(i)), i), i)

    def test_non_consecutive_elements(self):
        test_cases = [
            ([1, 2, 3, 4, 5], 5),
            ([1, 2, 3, 4, 5, 6], 6),
            ([1, 2, 3, 4, 5, 6, 7], 7),
            ([1, 2, 3, 4, 5, 6, 7, 8], 8),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9),
            ([1, 2, 3, 4, 5, 6, 7, 9, 8], 6),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9),
        ]
        for arr, n in test_cases:
            self.assertEqual(longest_subseq_with_diff_one(arr, len(arr)), len(arr))

    def test_negative_numbers(self):
        test_cases = [
            ([-1, -2, -3, -4, -5], 5),
            ([-1, -2, -3, -4, -5, -6], 6),
            ([-1, -2, -3, -4, -5, -6, -7], 7),
            ([-1, -2, -3, -4, -5, -6, -7, -8], 8),
            ([-1, -2, -3, -4, -5, -6, -7, -8, -9], 9),
            ([-1, -2, -3, -4, -5, -6, -7, -9, -8], 6),
            ([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 9),
        ]
        for arr, n in test_cases:
            self.assertEqual(longest_subseq_with_diff_one(arr, len(arr)), len(arr))

    def test_invalid_input(self):
        self.assertRaises(TypeError, longest_subseq_with_diff_one, [1, 2, 3], 'invalid string')
        self.assertRaises(TypeError, longest_subseq_with_diff_one, [1, 2, 3], 0.5)
        self.assertRaises(ValueError, longest_subseq_with_diff_one, [1, 2, 3], -1)
