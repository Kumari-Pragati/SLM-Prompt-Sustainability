import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 2, 4), 10)
        self.assertEqual(sum_Range_list([0, 0, 0, 0, 0], 2, 4), 0)
        self.assertEqual(sum_Range_list([-1, -2, -3, -4, -5], 2, 4), -10)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 0, 4), 10)
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 5, 5), 5)
        self.assertEqual(sum_Range_list([], 1, 2), 0)
        self.assertEqual(sum_Range_list([1], 1, 1), 1)

    def test_negative_index(self):
        self.assertRaises(IndexError, lambda: sum_Range_list([1, 2, 3], -1, 1))
        self.assertRaises(IndexError, lambda: sum_Range_list([1, 2, 3], 0, -1))
        self.assertRaises(IndexError, lambda: sum_Range_list([1, 2, 3], -2, 1))

    def test_invalid_input(self):
        self.assertRaises(TypeError, lambda: sum_Range_list('abc', 1, 2))
        self.assertRaises(TypeError, lambda: sum_Range_list([1, 2], 1.5, 2))
        self.assertRaises(TypeError, lambda: sum_Range_list([1, 2], 1, 'a') )
        self.assertRaises(TypeError, lambda: sum_Range_list([1, 2], 1, 2, 3))
