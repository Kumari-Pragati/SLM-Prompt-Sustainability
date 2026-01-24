import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 4), 10)
        self.assertEqual(sum_range_list([-1, -2, -3, -4, -5], 2, 4), -10)
        self.assertEqual(sum_range_list([0, 0, 0, 0, 0], 2, 4), 0)

    def test_edge_cases(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 5), 15)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 6, 5), 0)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 1), 1)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 0, 5), 15)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 5, 6), 0)

    def test_negative_inputs(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], -1, 5), 15)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 5, -1), 15)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], -2, -1), 0)

    def test_invalid_inputs(self):
        self.assertRaises(IndexError, lambda: sum_range_list([1, 2, 3], 3, 4))
        self.assertRaises(IndexError, lambda: sum_range_list([1, 2, 3], 0, -1))
        self.assertRaises(TypeError, lambda: sum_range_list('abc', 1, 2))
        self.assertRaises(TypeError, lambda: sum_range_list([1, 2], 1.5, 2))
