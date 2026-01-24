import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):
    def test_zero_value(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 0), 0)

    def test_single_coin(self):
        self.assertEqual(min_coins([1], 1, 1), 1)

    def test_multiple_coins(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 4), 2)

    def test_exceeds_max_value(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 10), sys.maxsize)

    def test_no_coins_found(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 5), sys.maxsize)

    def test_edge_case(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 3), 1)
