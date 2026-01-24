import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(coin_change([1, 2, 3], 3, 4), 1)

    def test_edge_case_S_zero(self):
        self.assertEqual(coin_change([1, 2, 3], 0, 4), 0)

    def test_edge_case_m_zero(self):
        self.assertEqual(coin_change([], 0, 4), 0)

    def test_edge_case_n_zero(self):
        self.assertEqual(coin_change([1, 2, 3], 3, 0), 0)

    def test_edge_case_S_j_zero(self):
        self.assertEqual(coin_change([0, 1, 2, 3], 3, 4), 1)

    def test_edge_case_m_one(self):
        self.assertEqual(coin_change([1], 1, 4), 1)

    def test_edge_case_n_one(self):
        self.assertEqual(coin_change([1], 3, 1), 1)

    def test_edge_case_S_j_greater_than_n(self):
        self.assertEqual(coin_change([1, 2, 3, 4], 3, 3), 1)

    def test_edge_case_m_greater_than_n(self):
        self.assertEqual(coin_change([1, 2, 3], 4, 3), 1)

    def test_edge_case_n_greater_than_m(self):
        self.assertEqual(coin_change([1, 2, 3], 3, 5), 1)

    def test_invalid_input_S_empty(self):
        with self.assertRaises(IndexError):
            coin_change([], 3, 4)

    def test_invalid_input_m_greater_than_n(self):
        with self.assertRaises(IndexError):
            coin_change([1, 2, 3], 5, 4)

    def test_invalid_input_n_greater_than_m(self):
        with self.assertRaises(IndexError):
            coin_change([1, 2, 3], 4, 5)
