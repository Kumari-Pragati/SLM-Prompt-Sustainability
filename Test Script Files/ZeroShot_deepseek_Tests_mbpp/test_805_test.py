import unittest
from mbpp_805_code import max_sum_list

class TestMaxSumList(unittest.TestCase):

    def test_max_sum_list(self):
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [7, 8, 9])
        self.assertEqual(max_sum_list([[1, 2], [3, 4], [5, 6]]), [5, 6])
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]), [10, 11, 12])
        self.assertEqual(max_sum_list([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]), [13, 14, 15])
        self.assertEqual(max_sum_list([[], [], []]), [])
        self.assertEqual(max_sum_list([[1], [2], [3]]), [3])
        self.assertEqual(max_sum_list([[1, 2], [3, 4], [5, 6], [7, 8]]), [7, 8])
