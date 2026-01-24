import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):

    def test_simple_sum(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(sum_list([0, 0, 0], [1, 2, 3]), [1, 2, 4])

    def test_empty_lists(self):
        self.assertEqual(sum_list([], []), [])
        self.assertEqual(sum_list([1], []), [1])
        self.assertEqual(sum_list([], [1]), [1])

    def test_different_lengths(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5]), [1+4, 2+5, 3+None])
        self.assertEqual(sum_list([1, 2], [3, 4, 5]), [1+3, 2+4])

    def test_negative_numbers(self):
        self.assertEqual(sum_list([-1, 2, -3], [-4, 5, -6]), [1, 7, -3])
        self.assertEqual(sum_list([-1, 0, -1], [1, 0, 1]), [0, 0, 0])
