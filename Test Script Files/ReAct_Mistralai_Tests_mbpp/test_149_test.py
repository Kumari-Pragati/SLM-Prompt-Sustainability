import unittest
from149_code import longest_subseq_with_diff_one

class TestLongestSubseqWithDiffOne(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(longest_subseq_with_diff_one([], 0), 0)

    def test_single_element(self):
        for element in range(10):
            self.assertEqual(longest_subseq_with_diff_one([element], 1), 1)

    def test_consecutive_elements(self):
        for i in range(1, 10):
            self.assertEqual(longest_subseq_with_diff_one(list(range(1, i+1)), i), i)

    def test_non_consecutive_elements(self):
        test_cases = [
            ([1, 2, 4, 5, 6], 5),
            ([1, 2, 3, 4, 5], 4),
            ([2, 3, 4, 5, 1], 4),
            ([1, 3, 5, 7, 9], 4),
            ([1, 2, 3, 4, 6], 3),
            ([1, 2, 3, 5, 7], 3),
            ([1, 2, 4, 6, 8], 3),
        ]
        for arr, n in test_cases:
            self.assertEqual(longest_subseq_with_diff_one(arr, len(arr)), sum(1 for i, j in zip(arr, arr[1:]) if abs(i - j) == 1))

    def test_negative_numbers(self):
        test_cases = [
            ([-1, -2, -3, -4, -5], 5),
            ([-1, -2, -3, -4, 5], 4),
            ([-1, -2, -3, 4, -5], 4),
            ([-1, -2, 3, 4, -5], 3),
            ([-1, 2, 3, 4, -5], 3),
            ([-1, 2, 3, 4, 5], 4),
        ]
        for arr, n in test_cases:
            self.assertEqual(longest_subseq_with_diff_one(arr, len(arr)), sum(1 for i, j in zip(arr, arr[1:]) if abs(i - j) == 1))

    def test_duplicates(self):
        test_cases = [
            ([1, 1, 2, 3, 4], 4),
            ([1, 1, 2, 2, 3], 3),
            ([1, 1, 2, 2, 2], 2),
            ([1, 2, 2, 2, 3], 3),
            ([1, 2, 2, 3, 3], 3),
            ([1, 2, 3, 3, 3], 3),
        ]
        for arr, n in test_cases:
            self.assertEqual(longest_subseq_with_diff_one(arr, len(arr)), sum(1 for i, j in zip(arr, arr[1:]) if abs(i - j) == 1))
