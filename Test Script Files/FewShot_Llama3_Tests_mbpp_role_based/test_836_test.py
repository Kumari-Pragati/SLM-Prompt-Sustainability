import unittest
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_sub_array_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4], 9), 6)

    def test_edge_case_empty_array(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)

    def test_edge_case_single_element_array(self):
        self.assertEqual(max_sub_array_sum([1], 1), 1)

    def test_edge_case_all_negative_array(self):
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4, -5], 5), -1)

    def test_edge_case_all_positive_array(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4, 5], 5), 5)

    def test_edge_case_array_with_zero(self):
        self.assertEqual(max_sub_array_sum([1, 0, 2, 3, 4], 5), 4)

    def test_edge_case_array_with_negative_and_positive(self):
        self.assertEqual(max_sub_array_sum([-1, 2, -3, 4, -1, 2, 1, -5, 4], 9), 6)
