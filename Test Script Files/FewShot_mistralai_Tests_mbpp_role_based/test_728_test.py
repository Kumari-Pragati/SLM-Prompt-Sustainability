import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_zero(self):
        self.assertEqual(sum_list([0, 0, 0], [0, 0, 0]), [0, 0, 0])

    def test_mixed_numbers(self):
        self.assertEqual(sum_list([1, 0, 3], [-2, 4, -1]), [3, 4, 2])

    def test_empty_lists(self):
        self.assertEqual(sum_list([], []), [])

    def test_different_lengths(self):
        self.assertRaises(IndexError, sum_list, [1, 2, 3], [4, 5])
