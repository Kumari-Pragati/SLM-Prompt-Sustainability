import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 4), 10)
        self.assertEqual(sum_range_list([6, 7, 8], 1, 3), 21)
        self.assertEqual(sum_range_list([-1, 0, 1], 1, 2), 0)

    def test_edge_case(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 1), 1)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 5, 5), 15)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 0, 4), 10)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 0, 0), 0)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 6, 6), 0)

    def test_boundary_case(self):
        self.assertEqual(sum_range_list([], 1, 1), 0)
        self.assertEqual(sum_range_list([1], 1, 1), 1)
        self.assertEqual(sum_range_list([1, 2], 2, 2), 2)
        self.assertEqual(sum_range_list([1, 2], 1, 2), 3)
        self.assertEqual(sum_range_list([1, 2], 0, 2), 2)
        self.assertEqual(sum_range_list([1, 2], 2, 0), 2)
