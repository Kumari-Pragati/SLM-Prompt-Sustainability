import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(max_sum_of_three_consecutive([1, -2, 3, 4, -5], 5), 12)
        self.assertEqual(max_sum_of_three_consecutive([0, 0, 0, 0, 0], 5), 0)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(max_sum_of_three_consecutive([1], 1), 1)
        self.assertEqual(max_sum_of_three_consecutive([1, 2], 2), 3)
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3], 3), 6)
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4], 4), 10)
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5], 1), 1)
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5], 6), 15)
        self.assertEqual(max_sum_of_three_consecutive([], 0), 0)
        self.assertEqual(max_sum_of_three_consecutive([-1], 1), -1)
        self.assertEqual(max_sum_of_three_consecutive([-1, -2], 2), -3)
