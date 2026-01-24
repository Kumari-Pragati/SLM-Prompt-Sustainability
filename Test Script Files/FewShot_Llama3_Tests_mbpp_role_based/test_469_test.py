import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):
    def test_typical_use_case(self):
        price = [1, 5, 3, 8, 12, 9, 18]
        k = 2
        self.assertEqual(max_profit(price, k), 10)

    def test_edge_case_k_zero(self):
        price = [1, 5, 3, 8, 12, 9, 18]
        k = 0
        self.assertEqual(max_profit(price, k), 0)

    def test_edge_case_price_empty(self):
        price = []
        k = 2
        with self.assertRaises(IndexError):
            max_profit(price, k)

    def test_edge_case_k_negative(self):
        price = [1, 5, 3, 8, 12, 9, 18]
        k = -1
        with self.assertRaises(ValueError):
            max_profit(price, k)

    def test_edge_case_price_single_element(self):
        price = [1]
        k = 2
        self.assertEqual(max_profit(price, k), 0)
