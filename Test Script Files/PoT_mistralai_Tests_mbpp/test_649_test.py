import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 2, 4), 15)

    def test_edge_case_min(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 1, 1), 1)

    def test_edge_case_max(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 5, 5), 5)

    def test_boundary_case_m_eq_n(self):
        self.assertEqual(sum_Range_list([1, 2, 3, 4, 5], 4, 4), 10)

    def test_empty_list(self):
        self.assertEqual(sum_Range_list([], 1, 2), 0)

    def test_negative_nums(self):
        self.assertEqual(sum_Range_list([-1, -2, -3, -4, -5], 2, 4), -15)

    def test_invalid_input_m_greater_than_n(self):
        self.assertRaises(IndexError, sum_Range_list, [1, 2, 3, 4, 5], 6, 4)

    def test_invalid_input_m_less_than_0(self):
        self.assertRaises(IndexError, sum_Range_list, [1, 2, 3, 4, 5], -1, 4)
