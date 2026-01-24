import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):
    def test_typical_case_even_sum(self):
        arr = [1, 2, 3, 4, 5]
        n = 5
        p = 1
        self.assertEqual(check_last(arr, n, p), "ODD")

    def test_typical_case_odd_sum(self):
        arr = [1, 2, 3, 4, 6]
        n = 5
        p = 1
        self.assertEqual(check_last(arr, n, p), "EVEN")

    def test_boundary_case_even_sum(self):
        arr = [2, 4, 6]
        n = 3
        p = 1
        self.assertEqual(check_last(arr, n, p), "EVEN")

    def test_boundary_case_odd_sum(self):
        arr = [1, 3, 5]
        n = 3
        p = 1
        self.assertEqual(check_last(arr, n, p), "ODD")

    def test_edge_case_zero(self):
        arr = [0, 0, 0]
        n = 3
        p = 1
        self.assertEqual(check_last(arr, n, p), "EVEN")

    def test_edge_case_negative_numbers(self):
        arr = [-1, -2, -3]
        n = 3
        p = 1
        self.assertEqual(check_last(arr, n, p), "ODD")

    def test_invalid_input_n_greater_than_arr_length(self):
        arr = [1, 2, 3]
        n = 4
        p = 1
        with self.assertRaises(IndexError):
            check_last(arr, n, p)

    def test_invalid_input_p_not_in_1_or_0(self):
        arr = [1, 2, 3]
        n = 3
        p = 2
        with self.assertRaises(ValueError):
            check_last(arr, n, p)
