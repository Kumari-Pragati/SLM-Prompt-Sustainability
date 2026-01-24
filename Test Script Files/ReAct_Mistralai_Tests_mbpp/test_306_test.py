import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum_increasing_subseq([], 0, 0, 0), 0)

    def test_single_element(self):
        for num in range(10):
            self.assertEqual(max_sum_increasing_subseq([num], 1, 0, 0), num)

    def test_increasing_sequence(self):
        data = [1, 2, 3, 4, 5]
        for i in range(len(data)):
            for k in range(i + 1, len(data)):
                self.assertEqual(max_sum_increasing_subseq(data, len(data), i, k), sum(data[i:k + 1]))

    def test_decreasing_sequence(self):
        data = [5, 4, 3, 2, 1]
        for i in range(len(data)):
            for k in range(i + 1, len(data)):
                self.assertEqual(max_sum_increasing_subseq(data, len(data), i, k), sum(data[i:k + 1]))

    def test_mixed_sequence(self):
        data = [1, 5, 2, 6, 3, 4]
        for i in range(len(data)):
            for k in range(i + 1, len(data)):
                self.assertLessEqual(max_sum_increasing_subseq(data, len(data), i, k), sum(data[i:k + 1]))

    def test_negative_numbers(self):
        data = [-1, -2, -3, 4]
        for i in range(len(data)):
            for k in range(i + 1, len(data)):
                self.assertLessEqual(max_sum_increasing_subseq(data, len(data), i, k), sum(data[i:k + 1]))

    def test_zero(self):
        data = [0, 1, 2, 3]
        for i in range(len(data)):
            for k in range(i + 1, len(data)):
                self.assertLessEqual(max_sum_increasing_subseq(data, len(data), i, k), sum(data[i:k + 1]))

    def test_index_out_of_range(self):
        with self.assertRaises(IndexError):
            max_sum_increasing_subseq([1, 2, 3], 3, 4, 0)

    def test_negative_index(self):
        with self.assertRaises(ValueError):
            max_sum_increasing_subseq([1, 2, 3], 3, -1, 0)

    def test_negative_k(self):
        with self.assertRaises(ValueError):
            max_sum_increasing_subseq([1, 2, 3], 3, 0, -1)
