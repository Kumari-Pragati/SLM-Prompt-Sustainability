import unittest
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, -2, 4, 5, -3, 6], 8), 5)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), 1)
        self.assertEqual(max_sub_array_sum([0, 3, 5, -2, 7, -8, 12, -9, 15], 9), 6)

    def test_edge_case_empty(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)
        self.assertEqual(max_sub_array_sum([-1], 1), 1)
        self.assertEqual(max_sub_array_sum([0], 1), 1)

    def test_edge_case_all_negative(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), 1)

    def test_edge_case_all_zero(self):
        self.assertEqual(max_sub_array_sum([0, 0, 0, 0, 0], 5), 1)

    def test_corner_case_all_positive_except_one(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, -5, 6, 7, 8, 9], 9), 6)

    def test_corner_case_all_negative_except_one(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, 5, -6, -7, -8, -9], 9), 1)
