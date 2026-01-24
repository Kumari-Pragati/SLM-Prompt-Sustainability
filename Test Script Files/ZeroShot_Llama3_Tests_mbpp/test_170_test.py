import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_sum_range_list(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 4), 9)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 3, 5), 9)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 1), 1)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 5, 5), 5)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 5), 15)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 2), 3)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 4, 4), 4)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 3, 3), 3)

    def test_sum_range_list_edge_cases(self):
        self.assertEqual(sum_range_list([], 1, 1), 0)
        self.assertEqual(sum_range_list([1], 1, 1), 1)
        self.assertEqual(sum_range_list([1, 2], 1, 2), 3)
        self.assertEqual(sum_range_list([1, 2, 3], 1, 1), 1)
        self.assertEqual(sum_range_list([1, 2, 3], 2, 2), 2)
        self.assertEqual(sum_range_list([1, 2, 3], 3, 3), 3)
