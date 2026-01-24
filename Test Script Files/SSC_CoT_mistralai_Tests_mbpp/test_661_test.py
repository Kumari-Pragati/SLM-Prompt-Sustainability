import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5], 5), [1, 3, 7, 12, 15])
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3, -4, -5], 5), [-1, -1, 1, -3, -7])
        self.assertEqual(max_sum_of_three_consecutive([0, 0, 0, 0, 0], 5), [0, 0, 0, 0, 0])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_sum_of_three_consecutive([1], 1), [1])
        self.assertEqual(max_sum_of_three_consecutive([1, 2], 2), [1, 3])
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3], 3), [1, 3, 6])
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6], 6), [1, 3, 6, 10, 15, 21])
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3, -4, -5], 1), [-1])
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3, -4, -5], 0), [None])

    def test_special_cases(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 2, 1], 5), [1, 3, 6, 8, 3])
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3, -2, -1], 5), [-1, -1, 1, -3, -5])
        self.assertEqual(max_sum_of_three_consecutive([0, 0, 0, 0, 0, 0], 6), [0, 0, 0, 0, 0, 0])
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7], 7), [1, 3, 6, 10, 15, 21, 28])
