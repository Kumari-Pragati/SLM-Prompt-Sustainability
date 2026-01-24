import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3], 3), 6)
        self.assertEqual(max_sum_of_three_consecutive([4, 5, 6], 3), 15)

    def test_edge_conditions(self):
        self.assertEqual(max_sum_of_three_consecutive([], 0), 0)
        self.assertEqual(max_sum_of_three_consecutive([1], 1), 1)
        self.assertEqual(max_sum_of_three_consecutive([1, 2], 2), 3)

    def test_boundary_conditions(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 39)
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3], 3), -1)

    def test_complex_cases(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 54)
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 10), -3)
