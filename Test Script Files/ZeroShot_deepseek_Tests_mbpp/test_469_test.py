import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_max_profit(self):
        self.assertEqual(max_profit([5, 2, 7, 3, 6, 1, 4], 3), 6)
        self.assertEqual(max_profit([10, 22, 5, 75, 65, 80], 2), 87)
        self.assertEqual(max_profit([100, 30, 15, 10, 8, 25, 100], 3), 100)
        self.assertEqual(max_profit([10, 20, 30, 40, 50, 60, 70], 1), 60)
        self.assertEqual(max_profit([100, 90, 80, 70, 60, 50, 40], 2), 0)
