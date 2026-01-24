import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 1, 3), 6)
        self.assertEqual(sum_Range_list([6, 7, 8], 2, 2), 7)
        self.assertEqual(sum_Range_list([-1, 0, 1], 1, 2), 0)

    def test_edge_and_boundary(self):
        self.assertEqual(sum_Range_list([], 1, 1), 0)
        self.assertEqual(sum_Range_list([1], 1, 1), 1)
        self.assertEqual(sum_Range_list([1, 2], 2, 2), 2)
        self.assertEqual(sum_Range_list([1, 2], 1, 2), 3)
        self.assertEqual(sum_Range_list([1, 2], 0, 2), 3)
        self.assertEqual(sum_Range_list([1, 2], 3, 3), 0)

    def test_complex(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 1, 5), 15)
        self.assertEqual(sum_Range_list([-1, 0, 1], 0, 2), 0)
        self.assertEqual(sum_Range_list([-1, 0, 1], -1, 2), 2)
        self.assertEqual(sum_Range_list([-1, 0, 1], -2, 2), 2)
        self.assertEqual(sum_Range_list([-1, 0, 1], -3, 2), 0)
