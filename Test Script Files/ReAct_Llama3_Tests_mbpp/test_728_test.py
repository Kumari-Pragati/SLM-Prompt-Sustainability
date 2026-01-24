import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):

    def test_sum_list_typical(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_sum_list_empty(self):
        self.assertEqual(sum_list([], []), [])

    def test_sum_list_single(self):
        self.assertEqual(sum_list([1], [2]), [3])

    def test_sum_list_long(self):
        self.assertEqual(sum_list([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]), [7, 9, 11, 13, 15])

    def test_sum_list_mismatched_length(self):
        with self.assertRaises(IndexError):
            sum_list([1, 2, 3], [4, 5])

    def test_sum_list_negative_numbers(self):
        self.assertEqual(sum_list([-1, 2, 3], [4, -5, 6]), [3, -1, 9])
