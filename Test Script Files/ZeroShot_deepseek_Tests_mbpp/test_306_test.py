import unittest
from mbpp_306_code import max_sum_increasing_subseq

class TestMaxSumIncreasingSubseq(unittest.TestCase):

    def test_max_sum_increasing_subseq(self):
        a = [1, 101, 2, 3, 100, 4, 5]
        n = len(a)
        index = 3
        k = 5
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 106)

        a = [5, 10, 40, 30, 20]
        n = len(a)
        index = 3
        k = 2
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 90)

        a = [1, 2, 3, 4, 5]
        n = len(a)
        index = 4
        k = 4
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 15)

        a = [1, 2, 3, 4, 5]
        n = len(a)
        index = 0
        k = 0
        self.assertEqual(max_sum_increasing_subseq(a, n, index, k), 1)
