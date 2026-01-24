import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_sum_range_list(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)
        self.assertEqual(sum_range_list([10, 20, 30, 40, 50], 0, 4), 150)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 4), 9)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 0, 0), 1)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 4), 12)
