import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):

    def test_typical_case_even_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 1), "ODD")

    def test_typical_case_odd_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4, 6], 5, 1), "EVEN")

    def test_typical_case_p_not_equal_to_1(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 0), "EVEN")

    def test_edge_case_empty_array(self):
        self.assertEqual(check_last([], 0, 1), "EVEN")

    def test_edge_case_single_element_array(self):
        self.assertEqual(check_last([5], 1, 1), "EVEN")

    def test_boundary_case_max_integer_array(self):
        self.assertEqual(check_last([2147483647], 1, 1), "EVEN")

    def test_invalid_input_negative_number_in_array(self):
        with self.assertRaises(IndexError):
            check_last([1, -2, 3, 4, 5], 5, 1)

    def test_invalid_input_negative_n(self):
        with self.assertRaises(IndexError):
            check_last([1, 2, 3, 4, 5], -1, 1)

    def test_invalid_input_p_not_0_or_1(self):
        with self.assertRaises(ValueError):
            check_last([1, 2, 3, 4, 5], 5, 2)
