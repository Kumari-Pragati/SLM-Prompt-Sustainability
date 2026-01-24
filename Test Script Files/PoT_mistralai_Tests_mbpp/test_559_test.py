import unittest
from mbpp_559_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, -2, 4, 5], 3), 12)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), -1)
        self.assertEqual(max_sub_array_sum([0, 0, 0, 0, 0], 5), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_sub_array_sum([], 1), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)
        self.assertEqual(max_sub_array_sum([-1], 1), -1)
        self.assertEqual(max_sub_array_sum([0], 1), 0)

    def test_edge_case_size_larger_than_list_length(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3], 4), 6)

    def test_edge_case_negative_size(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3], -1), 6)
