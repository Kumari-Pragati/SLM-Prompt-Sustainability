import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_typical_case(self):
        price = [10, 22, 5, 75, 65, 80]
        k = 2
        self.assertEqual(max_profit(price, k), 87)

    def test_typical_case_with_same_prices(self):
        price = [10, 10, 10, 10, 10]
        k = 2
        self.assertEqual(max_profit(price, k), 0)

    def test_boundary_case_with_zero_transactions(self):
        price = [10, 22, 5, 75, 65, 80]
        k = 0
        self.assertEqual(max_profit(price, k), 0)

    def test_boundary_case_with_zero_prices(self):
        price = []
        k = 2
        self.assertEqual(max_profit(price, k), 0)

    def test_error_case_with_negative_prices(self):
        price = [10, -22, 5, 75, 65, 80]
        k = 2
        with self.assertRaises(Exception):
            max_profit(price, k)

    def test_error_case_with_negative_transactions(self):
        price = [10, 22, 5, 75, 65, 80]
        k = -2
        with self.assertRaises(Exception):
            max_profit(price, k)
