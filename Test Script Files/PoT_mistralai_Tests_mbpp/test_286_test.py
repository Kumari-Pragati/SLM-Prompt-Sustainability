import unittest
from mbpp_286_code import max_sub_array_sum_repeated

class TestMaxSubArraySumRepeated(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3, 4, 5], 3, 2), 9)
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, 3, 4, -5], 5, 3), 12)
        self.assertEqual(max_sub_array_sum_repeated([0, 0, 0, 0], 4, 2), 0)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_sub_array_sum_repeated([], 3, 2), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sub_array_sum_repeated([1], 1, 1), 1)

    def test_edge_case_single_element_negative(self):
        self.assertEqual(max_sub_array_sum_repeated([-1], 1, 1), -1)

    def test_edge_case_k_greater_than_n(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], 2, 3), 6)

    def test_edge_case_k_less_than_1(self):
        self.assertEqual(max_sub_array_sum_repeated([1, 2, 3], 3, 0), 0)

    def test_corner_case_all_negative(self):
        self.assertEqual(max_sub_array_sum_repeated([-1, -2, -3], 3, 2), -1)
