import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):

    def test_typical_case_even_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 1), "ODD")

    def test_typical_case_odd_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 1), "EVEN")

    def test_boundary_case_even_sum(self):
        self.assertEqual(check_last([100], 1, 1), "ODD")

    def test_boundary_case_odd_sum(self):
        self.assertEqual(check_last([101], 1, 1), "EVEN")

    def test_edge_case_empty_array(self):
        self.assertEqual(check_last([], 0, 1), "EVEN")

    def test_edge_case_p_equals_0(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 0), "EVEN")

    def test_corner_case_large_array(self):
        self.assertEqual(check_last(list(range(1, 10001)), 10000, 1), "ODD")
