import unittest
from mbpp_649_code import sum_Range_list

class TestSumRangeList(unittest.TestCase):
    def test_typical_case(self):
        nums = [1, 2, 3, 4, 5]
        m = 1
        n = 4
        self.assertEqual(sum_Range_list(nums, m, n), 9)

    def test_edge_case_m_equal_n(self):
        nums = [1, 2, 3, 4, 5]
        m = 4
        n = 4
        self.assertEqual(sum_Range_list(nums, m, n), 4)

    def test_edge_case_m_greater_than_n(self):
        nums = [1, 2, 3, 4, 5]
        m = 5
        n = 2
        self.assertEqual(sum_Range_list(nums, m, n), 0)

    def test_edge_case_m_equal_to_zero(self):
        nums = [1, 2, 3, 4, 5]
        m = 0
        n = 4
        self.assertEqual(sum_Range_list(nums, m, n), 9)

    def test_edge_case_n_greater_than_length_of_list(self):
        nums = [1, 2, 3, 4, 5]
        m = 1
        n = 10
        self.assertEqual(sum_Range_list(nums, m, n), 9)

    def test_invalid_input_type_m(self):
        nums = [1, 2, 3, 4, 5]
        m = 'a'
        n = 4
        with self.assertRaises(TypeError):
            sum_Range_list(nums, m, n)

    def test_invalid_input_type_n(self):
        nums = [1, 2, 3, 4, 5]
        m = 1
        n = 'b'
        with self.assertRaises(TypeError):
            sum_Range_list(nums, m, n)
