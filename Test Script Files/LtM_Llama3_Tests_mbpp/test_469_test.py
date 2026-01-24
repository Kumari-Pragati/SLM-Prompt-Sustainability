import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):
    def test_simple_case(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 2), 4)

    def test_edge_case_zero_k(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 0), 0)

    def test_edge_case_zero_price(self):
        self.assertEqual(max_profit([], 2), 0)

    def test_edge_case_k_greater_than_price_length(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 10), 4)

    def test_edge_case_k_equal_to_price_length(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case_k_less_than_price_length(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 1), 4)

    def test_edge_case_k_equal_to_zero(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 0), 0)

    def test_edge_case_k_greater_than_price_length(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 10), 4)

    def test_edge_case_k_equal_to_price_length(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case_k_less_than_price_length(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 1), 4)

    def test_edge_case_k_equal_to_zero(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 0), 0)
