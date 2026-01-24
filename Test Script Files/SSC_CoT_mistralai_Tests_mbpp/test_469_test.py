import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_profit([10, 22, 34, 11, 5], 2), 19)
        self.assertEqual(max_profit([3, 5, 0, 3, 9, 3], 2), 9)
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 1), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(max_profit([], 1), 0)
        self.assertEqual(max_profit([1], 1), 0)
        self.assertEqual(max_profit([1, 2], 0), 0)
        self.assertEqual(max_profit([1, 2], 3), 0)
        self.assertEqual(max_profit([1, 2], 2), 1)
        self.assertEqual(max_profit([1, 2, 3], 0), 0)
        self.assertEqual(max_profit([1, 2, 3], 4), 0)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, max_profit, [1, 2], -1)
        self.assertRaises(TypeError, max_profit, [1, 2], 'k')
