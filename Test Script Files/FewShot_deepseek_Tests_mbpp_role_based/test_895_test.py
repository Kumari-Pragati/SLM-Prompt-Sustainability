import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(max_sum_subseq([5]), 5)

    def test_two_elements(self):
        self.assertEqual(max_sum_subseq([3, 7]), 10)
        self.assertEqual(max_sum_subseq([-3, -7]), -3)

    def test_multiple_elements(self):
        self.assertEqual(max_sum_subseq([2, 4, 6, 2, 5]), 13)
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        self.assertEqual(max_sum_subseq([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4, -5]), -1)

    def test_large_numbers(self):
        self.assertEqual(max_sum_subseq([100, 200, 300, 400]), 1000)
