import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):
    def test_typical_input(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 2
        n = 6
        self.assertEqual(sum_Range_list(nums, m, n), 18)

    def test_edge_case_m_equal_n(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 5
        n = 5
        self.assertEqual(sum_Range_list(nums, m, n), 15)

    def test_edge_case_m_greater_than_n(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 10
        n = 5
        self.assertEqual(sum_Range_list(nums, m, n), 15)

    def test_edge_case_m_equal_to_0(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 0
        n = 5
        self.assertEqual(sum_Range_list(nums, m, n), 15)

    def test_edge_case_n_greater_than_length_of_list(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 2
        n = 15
        self.assertEqual(sum_Range_list(nums, m, n), 18)

    def test_invalid_input_m_greater_than_n(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 7
        n = 3
        with self.assertRaises(IndexError):
            sum_Range_list(nums, m, n)
