import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_sum_subseq([]), 0)

    def test_single_element(self):
        for num in range(-10, 11):
            self.assertEqual(max_sum_subseq([num]), num)

    def test_positive_numbers(self):
        for i in range(1, 11):
            nums = [j for j in range(i)]
            self.assertEqual(max_sum_subseq(nums), sum(nums))

    def test_negative_numbers(self):
        for i in range(1, 11):
            nums = [-j for j in range(i)]
            self.assertEqual(max_sum_subseq(nums), sum(nums))

    def test_mixed_numbers(self):
        for i in range(1, 11):
            nums = [j for j in range(-i, i)]
            self.assertEqual(max_sum_subseq(nums), sum(nums))

    def test_negative_and_positive_numbers(self):
        for i in range(1, 11):
            nums = [j for j in range(-i, 0)] + [j for j in range(1, i + 1)]
            self.assertEqual(max_sum_subseq(nums), sum(nums))

    def test_zero(self):
        self.assertEqual(max_sum_subseq([0]), 0)
        self.assertEqual(max_sum_subseq([0, 0]), 0)
        self.assertEqual(max_sum_subseq([0, 0, 0]), 0)

    def test_large_numbers(self):
        for i in range(1, 11):
            nums = [j for j in range(10 ** i - 1, 10 ** i)]
            self.assertEqual(max_sum_subseq(nums), sum(nums))

    def test_large_negative_numbers(self):
        for i in range(1, 11):
            nums = [-j for j in range(10 ** i - 1, 0, -1)]
            self.assertEqual(max_sum_subseq(nums), sum(nums))

    def test_large_mixed_numbers(self):
        for i in range(1, 11):
            nums = [j for j in range(-10 ** i, 10 ** i)]
            self.assertEqual(max_sum_subseq(nums), sum(nums))
