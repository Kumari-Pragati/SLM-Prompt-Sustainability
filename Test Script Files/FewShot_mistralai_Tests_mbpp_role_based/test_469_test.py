import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_profit([10, 22, 5, 75, 65, 80]), 63)

    def test_edge_case_1(self):
        self.assertEqual(max_profit([1, 2, 3, 4]), 3)

    def test_edge_case_2(self):
        self.assertEqual(max_profit([10, 22, 5, 75, 65, 80, 100]), 90)

    def test_boundary_case_1(self):
        self.assertEqual(max_profit([10, 22, 5, 75, 65, 80], 0), 0)

    def test_boundary_case_2(self):
        self.assertEqual(max_profit([10, 22, 5, 75, 65, 80], 6), 63)

    def test_boundary_case_3(self):
        self.assertEqual(max_profit([], 1), 0)

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            max_profit('not a list', 1)

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            max_profit([1, 2, 3], 'not an integer')
