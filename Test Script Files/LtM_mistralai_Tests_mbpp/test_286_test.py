import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4], 3, 2), 9)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4], 4, 2), -1)
        self.assertEqual(max_sub_array_sum_repeated([0, 0, 0, 0], 4, 4), 0)

    def test_edge_cases(self):
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 1), 1)
        self.assertEqual(max_sub_array_sum_repeated([1, 2], 2, 1), 3)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], 3, 1), 6)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], 3, 2), 9)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3], 3, 2), -1)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3], 3, 3), -1)

    def test_boundary_conditions(self):
        self.assertEqual(max_sub_array_sum_repeated([], 0, 1), 0)
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 0), 0)
        self.assertEqual(max_sub_array_sum_repeated([1], 0, 1), 0)
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 0), 0)
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 2), 0)
