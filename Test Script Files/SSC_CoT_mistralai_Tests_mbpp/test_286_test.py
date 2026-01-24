import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 5, 2), 15)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3, -4, -5], 5, 2), 5)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5, 6], 6, 2), 15)

    def test_edge_cases(self):
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 1), 1)
        self.assertEqual(max_sub_array_sum_repeated([1, 2], 2, 1), 3)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], 3, 1), 6)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], 2, 2), 6)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], 1, 3), 3)

    def test_boundary_cases(self):
        self.assertEqual(max_sub_array_sum_repeated([], 0, 1), 0)
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 0), 1)
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 2), 1)
        self.assertEqual(max_sub_array_sum_repeated([1, 2], 1, 0), 2)
        self.assertEqual(max_sub_array_sum_repeated([1, 2], 1, 2), 2)

    def test_negative_inputs(self):
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3], 3, 1), -1)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3], 2, 2), -1)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3], 1, 3), -1)
