import unittest
from mbpp_895_code import max_sum_subseq

class TestMaxSumSubseq(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(max_sum_subseq([5]), 5)

    def test_two_elements(self):
        self.assertEqual(max_sum_subseq([5, 10]), 15)
        self.assertEqual(max_sum_subseq([10, 5]), 15)

    def test_multiple_elements(self):
        self.assertEqual(max_sum_subseq([1, 2, 3, 4]), 10)
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4]), 0)
        self.assertEqual(max_sum_subseq([-1, 2, -3, 4]), 5)

    def test_empty_list(self):
        self.assertEqual(max_sum_subseq([]), None)  # Assuming the function returns None for empty list

    def test_negative_numbers(self):
        self.assertEqual(max_sum_subseq([-1, -2, -3, -4]), 0)

    def test_large_numbers(self):
        self.assertEqual(max_sum_subseq([1000, 2000, 3000]), 6000)

    def test_duplicates(self):
        self.assertEqual(max_sum_subseq([1, 2, 3, 1]), 5)
