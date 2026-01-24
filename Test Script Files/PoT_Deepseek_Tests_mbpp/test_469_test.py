import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_profit([5, 2, 7, 3, 6, 1, 4], 3), 6)

    def test_edge_case_k_zero(self):
        self.assertEqual(max_profit([5, 2, 7, 3, 6, 1, 4], 0), 0)

    def test_edge_case_k_equal_to_n(self):
        self.assertEqual(max_profit([5, 2, 7, 3, 6, 1, 4], 7), 6)

    def test_edge_case_single_price(self):
        self.assertEqual(max_profit([5], 3), 0)

    def test_corner_case_decreasing_prices(self):
        self.assertEqual(max_profit([7, 6, 5, 4, 3, 2, 1], 3), 0)

    def test_corner_case_increasing_prices(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7], 3), 6)

    def test_corner_case_same_prices(self):
        self.assertEqual(max_profit([5, 5, 5, 5, 5, 5, 5], 3), 0)

    def test_invalid_input_empty_prices(self):
        with self.assertRaises(Exception):
            max_profit([], 3)

    def test_invalid_input_negative_k(self):
        with self.assertRaises(Exception):
            max_profit([5, 2, 7, 3, 6, 1, 4], -1)
