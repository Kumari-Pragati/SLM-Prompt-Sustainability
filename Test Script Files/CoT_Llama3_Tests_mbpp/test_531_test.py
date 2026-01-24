import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):

    def test_min_coins_zero(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 0), 0)

    def test_min_coins_one(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 1), 1)

    def test_min_coins_multiple(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 4), 2)

    def test_min_coins_large(self):
        self.assertEqual(min_coins([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 100), 10)

    def test_min_coins_invalid_input(self):
        with self.assertRaises(TypeError):
            min_coins([1, 2, 3], 'a', 4)

    def test_min_coins_edge_case(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 3), 1)

    def test_min_coins_edge_case_two(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 2), 1)
