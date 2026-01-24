import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):
    def test_typical_case(self):
        price = [10, 22, 5, 75, 65, 80]
        k = 2
        self.assertEqual(max_profit(price, k), 87)

    def test_boundary_case(self):
        price = [10, 22, 5, 75, 65, 80]
        k = 0
        self.assertEqual(max_profit(price, k), 0)

    def test_edge_case(self):
        price = [10, 22, 5, 75, 65, 80]
        k = 1
        self.assertEqual(max_profit(price, k), 75)

    def test_invalid_input(self):
        price = [10, 22, 5, 75, 65, 80]
        k = -1
        with self.assertRaises(ValueError):
            max_profit(price, k)
