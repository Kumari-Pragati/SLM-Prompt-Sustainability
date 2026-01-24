import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 1), "EVEN")

    def test_edge_case_sum_even(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 1), "EVEN")

    def test_edge_case_sum_odd(self):
        self.assertEqual(check_last([1, 2, 3, 4, 6], 5, 1), "ODD")

    def test_edge_case_p_0(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 0), "EVEN")

    def test_edge_case_p_2(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 2), "EVEN")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_last("hello", 5, 1)

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            check_last([1, 2, 3, 4, 5], "five", 1)
