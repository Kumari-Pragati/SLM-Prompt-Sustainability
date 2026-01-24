import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(max_profit([10, 20, 30, 40], 2), 20)
        self.assertEqual(max_profit([9, 11, 8, 12], 1), 3)

    def test_edge_input(self):
        self.assertEqual(max_profit([], 1), 0)
        self.assertEqual(max_profit([1], 1), 0)
        self.assertEqual(max_profit([1, 2], 0), 0)

    def test_boundary_input(self):
        self.assertEqual(max_profit([1, 2, 3], 0), 0)
        self.assertEqual(max_profit([1, 2, 3], 10), 3)
        self.assertEqual(max_profit([1, 2, 3], 1), 2)

    def test_complex_input(self):
        self.assertEqual(max_profit([1, 5, 2, 6, 3, 4], 2), 5)
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 3), 4)
