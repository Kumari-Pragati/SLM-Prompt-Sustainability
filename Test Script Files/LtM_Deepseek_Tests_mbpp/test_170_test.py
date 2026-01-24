import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)

    def test_boundary_conditions(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 0, 0), 1)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 4, 4), 5)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 0, 4), 15)

    def test_edge_cases(self):
        self.assertEqual(sum_range_list([], 0, 0), 0)
        self.assertEqual(sum_range_list([1], 0, 0), 1)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], -1, 4), 15)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 5, 10), 0)
