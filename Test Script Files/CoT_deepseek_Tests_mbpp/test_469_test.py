import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_profit([10, 22, 5, 75, 65, 80], 2), 87)

    def test_typical_case_2(self):
        self.assertEqual(max_profit([100, 180, 260, 310, 40, 535, 695], 3), 605)

    def test_boundary_case(self):
        self.assertEqual(max_profit([10, 22, 5, 75, 65, 80], 0), 0)

    def test_edge_case(self):
        self.assertEqual(max_profit([], 2), None)
        self.assertEqual(max_profit([10, 22, 5, 75, 65, 80], -1), None)
        self.assertEqual(max_profit([10, 22, 5, 75, 65, 80], 7), None)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_profit("10, 22, 5, 75, 65, 80", 2)
        with self.assertRaises(TypeError):
            max_profit([10, 22, 5, 75, 65, 80], "2")
