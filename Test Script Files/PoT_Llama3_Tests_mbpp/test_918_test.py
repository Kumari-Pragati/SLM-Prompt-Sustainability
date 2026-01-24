import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(coin_change([1, 2, 3], 3, 4), 1)

    def test_edge_case_zero_sum(self):
        self.assertEqual(coin_change([1, 2, 3], 0, 4), 0)

    def test_edge_case_zero_denominators(self):
        self.assertEqual(coin_change([], 0, 4), 0)

    def test_edge_case_zero_n(self):
        self.assertEqual(coin_change([1, 2, 3], 3, 0), 0)

    def test_edge_case_zero_m(self):
        self.assertEqual(coin_change([1, 2, 3], 0, 4), 0)

    def test_edge_case_single_denominator(self):
        self.assertEqual(coin_change([1], 1, 4), 1)

    def test_edge_case_single_denominator_zero(self):
        self.assertEqual(coin_change([1], 0, 4), 0)

    def test_edge_case_single_denominator_zero_n(self):
        self.assertEqual(coin_change([1], 0, 0), 0)

    def test_edge_case_single_denominator_zero_m(self):
        self.assertEqual(coin_change([1], 1, 0), 0)

    def test_edge_case_single_denominator_zero_m_n(self):
        self.assertEqual(coin_change([1], 0, 0), 0)
