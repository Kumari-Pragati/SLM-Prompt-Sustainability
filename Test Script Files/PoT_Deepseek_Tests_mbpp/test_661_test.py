import unittest
from mbpp_661_code import max_sum_of_three_consecutive

class TestMaxSumOfThreeConsecutive(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5], 5), 12)
        self.assertEqual(max_sum_of_three_consecutive([-1, -2, -3, -4, -5], 5), -3)
        self.assertEqual(max_sum_of_three_consecutive([10, 20, 30, 40, 50], 5), 120)

    def test_edge_cases(self):
        self.assertEqual(max_sum_of_three_consecutive([], 0), 0)
        self.assertEqual(max_sum_of_three_consecutive([1], 1), 1)
        self.assertEqual(max_sum_of_three_consecutive([1, 2], 2), 3)

    def test_boundary_cases(self):
        self.assertEqual(max_sum_of_three_consecutive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 45)
        self.assertEqual(max_sum_of_three_consecutive([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1], 10), -5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_sum_of_three_consecutive("not a list", 5)
        with self.assertRaises(TypeError):
            max_sum_of_three_consecutive([1, 2, 3], "not an integer")
