import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_typical_case(self):
        price = [1, 5, 3, 8, 12, 9]
        k = 2
        self.assertEqual(max_profit(price, k), 7)

    def test_edge_case_k_zero(self):
        price = [1, 5, 3, 8, 12, 9]
        k = 0
        self.assertEqual(max_profit(price, k), 0)

    def test_edge_case_price_zero(self):
        price = [0, 0, 0, 0, 0, 0]
        k = 2
        self.assertEqual(max_profit(price, k), 0)

    def test_edge_case_k_greater_than_price_length(self):
        price = [1, 5, 3, 8, 12, 9]
        k = 10
        self.assertEqual(max_profit(price, k), 7)

    def test_edge_case_k_negative(self):
        price = [1, 5, 3, 8, 12, 9]
        k = -1
        with self.assertRaises(ValueError):
            max_profit(price, k)

    def test_edge_case_price_negative(self):
        price = [-1, 5, 3, 8, 12, 9]
        k = 2
        with self.assertRaises(ValueError):
            max_profit(price, k)

    def test_edge_case_price_empty(self):
        price = []
        k = 2
        with self.assertRaises(IndexError):
            max_profit(price, k)

    def test_edge_case_k_empty(self):
        price = [1, 5, 3, 8, 12, 9]
        k = []
        with self.assertRaises(TypeError):
            max_profit(price, k)
