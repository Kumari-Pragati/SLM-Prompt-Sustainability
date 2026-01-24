import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_profit([5, 1, 6, 2, 7], 2), 6)
        self.assertEqual(max_profit([10, 22, 5, 75, 65, 80], 2), 87)

    def test_edge_conditions(self):
        self.assertEqual(max_profit([], 2), 0)
        self.assertEqual(max_profit([5, 1, 6, 2, 7], 0), 0)
        self.assertEqual(max_profit([5, 1, 6, 2, 7], 1), 5)

    def test_boundary_conditions(self):
        self.assertEqual(max_profit([5, 1, 6, 2, 7], 3), 6)
        self.assertEqual(max_profit([100, 90, 80, 70, 60], 5), 0)

    def test_complex_cases(self):
        self.assertEqual(max_profit([10, 22, 5, 75, 65, 80], 3), 87)
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 4), 4)
