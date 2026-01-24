import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(max_profit([1, 5, 3, 5], 2), 4)
        self.assertEqual(max_profit([1, 5, 3, 5], 1), 4)
        self.assertEqual(max_profit([1, 2, 3, 4], 0), 0)
        self.assertEqual(max_profit([1, 2, 3, 4], 3), 3)
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 4), 4)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6], 5), 5)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7], 6), 6)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8], 7), 7)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9], 8), 8)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9), 9)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 10), 10)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 11), 11)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 12), 12)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 13), 13)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 14), 14)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 15), 15)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 16), 16)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 17), 17)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 18), 18)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 19), 19)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 20), 20)
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17