import unittest
from mbpp_170_code import sum_range_list

class TestSumRangeList(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 3), 6)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 2, 4), 9)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 3, 5), 10)

    def test_edge_cases(self):
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 1), 1)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 5, 5), 5)
        self.assertEqual(sum_range_list([1, 2, 3, 4, 5], 1, 5), 15)

    def test_invalid_inputs(self):
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], 6, 6)
        with self.assertRaises(IndexError):
            sum_range_list([1, 2, 3, 4, 5], 0, 0)
