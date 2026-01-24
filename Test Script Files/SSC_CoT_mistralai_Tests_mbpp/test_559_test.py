import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 3), 12)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 3), -3)
        self.assertEqual(max_sub_array_sum([1, 0, -1, 2, -3, 4, -5], 4), 6)

    def test_edge_cases(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)
        self.assertEqual(max_sub_array_sum([1], 1), 1)
        self.assertEqual(max_sub_array_sum([1, 2], 2), 3)
        self.assertEqual(max_sub_array_sum([1, 2, 3], 1), 1)
        self.assertEqual(max_sub_array_sum([1, 2, 3], 4), 6)
        self.assertEqual(max_sub_array_sum([-1, -2, -3], 1), -1)
        self.assertEqual(max_sub_array_sum([-1, -2, -3], 3), -3)

    def test_negative_array(self):
        self.assertEqual(max_sub_array_sum([-5, -3, -1], 3), -1)
        self.assertEqual(max_sub_array_sum([-5, -3, -1, -7, -9], 3), -3)
        self.assertEqual(max_sub_array_sum([-5, -3, -1, -7, -9, -11], 3), -3)

    def test_invalid_input(self):
        self.assertRaises(ValueError, max_sub_array_sum, [], -1)
        self.assertRaises(ValueError, max_sub_array_sum, [1], 0)
        self.assertRaises(ValueError, max_sub_array_sum, [1], -1)
