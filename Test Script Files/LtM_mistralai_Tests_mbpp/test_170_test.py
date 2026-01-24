import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)
        self.assertEqual(sum_range_list([10, 20, 30, 40, 50], 2, 4), 90)

    def test_edge_input(self):
        self.assertEqual(sum_range_list([], 1, 1), 0)
        self.assertEqual(sum_range_list([1], 1, 1), 1)
        self.assertEqual(sum_range_list([1, 2], 2, 2), 3)
        self.assertEqual(sum_range_list([1, 2], 1, 2), 3)
        self.assertEqual(sum_range_list([1, 2], 0, 1), 1)
        self.assertEqual(sum_range_list([1, 2], 2, 3), 3)
        self.assertEqual(sum_range_list([1, 2], 3, 3), 2)

    def test_complex_input(self):
        self.assertEqual(sum_range_list([1, 2, 3, -4, 5], 1, 4), 10)
        self.assertEqual(sum_range_list([1, 2, 3, -4, 5], 4, 4), -1)
        self.assertEqual(sum_range_list([1, 2, 3, -4, 5], 0, 4), 9)
        self.assertEqual(sum_range_list([1, 2, 3, -4, 5], 5, 5), 5)
