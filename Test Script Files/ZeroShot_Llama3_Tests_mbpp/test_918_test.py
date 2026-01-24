import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_coin_change(self):
        self.assertEqual(coin_change(3, 4, 5), 1)
        self.assertEqual(coin_change(10, 3, 10), 2)
        self.assertEqual(coin_change(11, 3, 11), 0)
        self.assertEqual(coin_change(12, 4, 12), 1)
        self.assertEqual(coin_change(15, 5, 15), 3)

    def test_coin_change_invalid_input(self):
        with self.assertRaises(TypeError):
            coin_change('a', 4, 5)
        with self.assertRaises(TypeError):
            coin_change(3, 'a', 5)
        with self.assertRaises(TypeError):
            coin_change(3, 4, 'a')
