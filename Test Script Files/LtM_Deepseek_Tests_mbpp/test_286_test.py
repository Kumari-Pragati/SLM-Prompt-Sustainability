import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], 3, 1), 6)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3], 3, 1), -1)
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4, 5], 5, 2), 6)

    def test_edge_conditions(self):
        self.assertEqual(max_sub_array_sum_repeated([], 0, 1), 0)
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 1), 1)
        self.assertEqual(max_sub_array_sum_repeated([-1], 1, 1), -1)
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], 3, 0), 0)

    def test_boundary_conditions(self):
        self.assertEqual(max_sub_array_sum_repeated([10000000], 1, 10000000), 10000000000000)
        self.assertEqual(max_sub_array_sum_repeated([-10000000], 1, 10000000), -10000000)
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4, 5], 5, 10000000), 6)

    def test_complex_cases(self):
        self.assertEqual(max_sub_array_sum_repeated([-2, -3, 4, -1, -2, 1, 5, -3], 8, 2), 7)
        self.assertEqual(max_sub_array_sum_repeated([1, -2, 3, -4, 5, -6, 7, -8, 9], 9, 3), 15)
