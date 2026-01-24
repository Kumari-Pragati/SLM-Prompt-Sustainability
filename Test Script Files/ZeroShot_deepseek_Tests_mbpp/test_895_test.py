import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(max_sum_subseq([5]), 5)

    def test_two_elements(self):
        self.assertEqual(max_sum_subseq([5, 10]), 15)
        self.assertEqual(max_sum_subseq([10, 5]), 15)

    def test_multiple_elements(self):
        self.assertEqual(max_sum_subseq([5, 10, 15]), 30)
        self.assertEqual(max_sum_subseq([10, 5, 15]), 30)
        self.assertEqual(max_sum_subseq([10, 10, 10]), 30)
        self.assertEqual(max_sum_subseq([-5, 10, 15]), 30)

    def test_negative_elements(self):
        self.assertEqual(max_sum_subseq([-5, -10, -15]), 0)
        self.assertEqual(max_sum_subseq([-5, 10, -15]), 10)

    def test_empty_list(self):
        self.assertEqual(max_sum_subseq([]), None)
