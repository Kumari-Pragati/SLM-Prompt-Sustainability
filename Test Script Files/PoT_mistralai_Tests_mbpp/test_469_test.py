import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(max_profit([10, 22, 5, 75, 65, 80]), 63)
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 0)

    def test_edge_cases(self):
        self.assertEqual(max_profit([], 1), 0)
        self.assertEqual(max_profit([1], 1), 0)
        self.assertEqual(max_profit([1, 2], 2), 1)
        self.assertEqual(max_profit([1, 2, 3], 3), 2)
        self.assertEqual(max_profit([1, 2, 3], 4), 2)
        self.assertEqual(max_profit([1, 2, 3], 5), 2)

    def test_corner_cases(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6], 0), 0)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6], 6), 5)
        self.assertEqual(max_profit([1, 2, 3, -4, 5, 6], 2), 3)
        self.assertEqual(max_profit([1, -2, 3, -4, 5, 6], 2), 4)
