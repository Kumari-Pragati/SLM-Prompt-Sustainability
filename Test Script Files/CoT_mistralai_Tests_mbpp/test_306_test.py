import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum_increasing_subseq([], 0, 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sum_increasing_subseq([1], 1, 0, 0), 1)

    def test_increasing_sequence(self):
        self.assertEqual(max_sum_increasing_subseq([1, 2, 3, 4, 5], 5, 4, 4), 12)

    def test_decreasing_sequence(self):
        self.assertEqual(max_sum_increasing_subseq([5, 4, 3, 2, 1], 5, 4, 4), 9)

    def test_mixed_sequence(self):
        self.assertEqual(max_sum_increasing_subseq([1, 5, 2, 3, 4], 5, 4, 4), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_increasing_subseq([-1, -2, -3, -4, -5], 5, 4, 4), -1)

    def test_invalid_index(self):
        with self.assertRaises(IndexError):
            max_sum_increasing_subseq([1, 2, 3], 3, 4, 0)

    def test_invalid_k(self):
        with self.assertRaises(IndexError):
            max_sum_increasing_subseq([1, 2, 3], 3, 0, 4)
