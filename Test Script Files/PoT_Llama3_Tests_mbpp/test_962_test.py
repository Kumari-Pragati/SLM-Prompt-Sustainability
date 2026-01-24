import unittest
from mbpp_962_code import sum_Even

class TestSumEven(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum_Even(1, 10), 25)

    def test_edge_case_l_equal_r(self):
        self.assertEqual(sum_Even(5, 5), 0)

    def test_edge_case_l_greater_than_r(self):
        self.assertEqual(sum_Even(10, 5), 0)

    def test_edge_case_l_equal_r_half(self):
        self.assertEqual(sum_Even(5, 5), 5)

    def test_edge_case_l_greater_than_r_half(self):
        self.assertEqual(sum_Even(10, 5), 5)

    def test_edge_case_l_zero(self):
        with self.assertRaises(ValueError):
            sum_Even(0, 5)

    def test_edge_case_r_zero(self):
        with self.assertRaises(ValueError):
            sum_Even(5, 0)

    def test_edge_case_l_negative(self):
        with self.assertRaises(ValueError):
            sum_Even(-5, 10)

    def test_edge_case_r_negative(self):
        with self.assertRaises(ValueError):
            sum_Even(5, -10)
