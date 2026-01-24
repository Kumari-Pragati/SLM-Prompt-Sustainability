import unittest
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), 1)
        self.assertEqual(max_sub_array_sum([0, 3, -2, 0, 4, 5, -9, 12, 0, -3, 5, 6], 12), 7)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)
        self.assertEqual(max_sub_array_sum([0], 1), 1)
        self.assertEqual(max_sub_array_sum([-1], 1), 1)
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 1), 1)
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 6), 5)
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 7), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), 1)
        self.assertEqual(max_sub_array_sum([-1, 0, -2, 1, -3, 2, -4, 3, -5, 4], 11), 6)

    def test_zero_numbers(self):
        self.assertEqual(max_sub_array_sum([0, 0, 0], 3), 1)
        self.assertEqual(max_sub_array_sum([0, 0, 0, 0], 4), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_sub_array_sum(1.23, 5)
        with self.assertRaises(TypeError):
            max_sub_array_sum([1, 2, 3], 4.5)
        with self.assertRaises(ValueError):
            max_sub_array_sum([], -1)
        with self.assertRaises(ValueError):
            max_sub_array_sum([1], 0)
