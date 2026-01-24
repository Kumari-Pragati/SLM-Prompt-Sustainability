import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 10)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 0)
        self.assertEqual(max_sub_array_sum([1, -2, 3, -4], 4), 3)

    def test_edge_conditions(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)
        self.assertEqual(max_sub_array_sum([1], 1), 1)
        self.assertEqual(max_sub_array_sum([-1], 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(max_sub_array_sum([1000000000, -1000000000], 2), 2000000000)
        self.assertEqual(max_sub_array_sum([-1000000000, 1000000000], 2), 1000000000)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 0)

    def test_complex_cases(self):
        self.assertEqual(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8), 7)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 0)
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5, 6, 7, 8], 8), 36)
