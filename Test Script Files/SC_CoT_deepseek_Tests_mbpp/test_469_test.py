import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_profit([10, 22, 5, 75, 65, 80], 2), 87)

    def test_edge_case_single_price(self):
        self.assertEqual(max_profit([10], 1), 0)

    def test_edge_case_no_transactions(self):
        self.assertEqual(max_profit([10, 20, 30, 40, 50], 0), 0)

    def test_edge_case_k_greater_than_prices(self):
        self.assertEqual(max_profit([10, 20, 30, 40, 50], 6), 45)

    def test_corner_case_decreasing_prices(self):
        self.assertEqual(max_profit([50, 40, 30, 20, 10], 2), 0)

    def test_corner_case_increasing_prices(self):
        self.assertEqual(max_profit([10, 20, 30, 40, 50], 2), 30)

    def test_invalid_input_empty_prices(self):
        with self.assertRaises(Exception):
            max_profit([], 2)

    def test_invalid_input_negative_prices(self):
        with self.assertRaises(Exception):
            max_profit([10, -20, 30, 40, 50], 2)
