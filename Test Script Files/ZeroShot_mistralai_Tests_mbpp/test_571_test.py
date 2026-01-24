import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessthanK(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([], 0, 0), 0)

    def test_single_element(self):
        for k in range(0, 10):
            self.assertEqual(max_sum_pair_diff_lessthan_K([1], 1, k), 1)

    def test_two_elements(self):
        for k in range(0, 10):
            self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2], 2, k), 3)

    def test_multiple_elements(self):
        test_cases = [
            (([1, 2, 3, 4], 4, 1), 10),
            (([1, 2, 3, 4], 4, 2), 9),
            (([1, 2, 3, 4], 4, 3), 8),
            (([1, 2, 3, 4], 4, 4), 7),
            (([1, 2, 3, 4], 4, 5), 6),
            (([1, 2, 3, 4], 4, 6), 4),
            (([1, 2, 3, 4], 4, 7), 2),
            (([1, 2, 3, 4], 4, 8), 0),
            (([1, 2, 3, 4], 4, 9), 0),
            (([1, 2, 3, 4], 4, 10), 0),

            (([1, 2, 3, 4, 5], 5, 1), 15),
            (([1, 2, 3, 4, 5], 5, 2), 14),
            (([1, 2, 3, 4, 5], 5, 3), 13),
            (([1, 2, 3, 4, 5], 5, 4), 12),
            (([1, 2, 3, 4, 5], 5, 5), 11),
            (([1, 2, 3, 4, 5], 5, 6), 10),
            (([1, 2, 3, 4, 5], 5, 7), 9),
            (([1, 2, 3, 4, 5], 5, 8), 8),
            (([1, 2, 3, 4, 5], 5, 9), 7),
            (([1, 2, 3, 4, 5], 5, 10), 6),
        ]
        for arr, N, K, expected in test_cases:
            self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), expected)
