import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):

    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(sum_list([0, 0, 0], [1, 1, 1]), [1, 1, 1])
        self.assertEqual(sum_list([-1, -2, -3], [-4, -5, -6]), [-5, -7, -9])
        self.assertEqual(sum_list([], []), [])
        self.assertEqual(sum_list([1], [2]), [3])
