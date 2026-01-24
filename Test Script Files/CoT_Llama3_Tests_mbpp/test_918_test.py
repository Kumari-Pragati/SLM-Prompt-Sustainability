import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):
    def test_coin_change_typical(self):
        self.assertEqual(coin_change(2, 3, 4), 1)

    def test_coin_change_edge(self):
        self.assertEqual(coin_change(0, 3, 4), 0)

    def test_coin_change_edge2(self):
        self.assertEqual(coin_change(4, 3, 4), 1)

    def test_coin_change_edge3(self):
        self.assertEqual(coin_change(5, 3, 4), 0)

    def test_coin_change_edge4(self):
        self.assertEqual(coin_change(1, 3, 4), 1)

    def test_coin_change_edge5(self):
        self.assertEqual(coin_change(3, 3, 4), 1)

    def test_coin_change_invalid_input1(self):
        with self.assertRaises(IndexError):
            coin_change(2, -3, 4)

    def test_coin_change_invalid_input2(self):
        with self.assertRaises(IndexError):
            coin_change(2, 3, -4)

    def test_coin_change_invalid_input3(self):
        with self.assertRaises(IndexError):
            coin_change(-2, 3, 4)

    def test_coin_change_invalid_input4(self):
        with self.assertRaises(IndexError):
            coin_change(2, 3, 0)
