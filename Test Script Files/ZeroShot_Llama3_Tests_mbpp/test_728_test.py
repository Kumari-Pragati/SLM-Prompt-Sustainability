import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):

    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(sum_list([-1, 0, 1], [1, 2, 3]), [0, 2, 4])
        self.assertEqual(sum_list([1, 2, 3], [-1, -2, -3]), [0, 0, 0])
        self.assertEqual(sum_list([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(sum_list([], [1, 2, 3]), [])

    def test_sum_list_empty(self):
        self.assertEqual(sum_list([], []), [])

    def test_sum_list_diff_len(self):
        with self.assertRaises(IndexError):
            sum_list([1, 2, 3], [4, 5])
