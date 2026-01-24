import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_profit([1, 5, 3, 8, 12, 9, 18, 20], 2), 19)

    def test_edge_case_k_zero(self):
        self.assertEqual(max_profit([1, 5, 3, 8, 12, 9, 18, 20], 0), 0)

    def test_edge_case_n_zero(self):
        self.assertEqual(max_profit([], 2), 0)

    def test_edge_case_k_n_zero(self):
        self.assertEqual(max_profit([1], 0), 0)

    def test_edge_case_k_n_one(self):
        self.assertEqual(max_profit([1], 1), 0)

    def test_edge_case_k_n_two(self):
        self.assertEqual(max_profit([1, 2], 2), 1)

    def test_edge_case_k_n_three(self):
        self.assertEqual(max_profit([1, 2, 3], 3), 2)

    def test_edge_case_k_n_four(self):
        self.assertEqual(max_profit([1, 2, 3, 4], 4), 3)

    def test_edge_case_k_n_five(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case_k_n_six(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6], 6), 5)

    def test_edge_case_k_n_seven(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7], 7), 6)

    def test_edge_case_k_n_eight(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8], 8), 7)

    def test_edge_case_k_n_nine(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 8)

    def test_edge_case_k_n_ten(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 9)
