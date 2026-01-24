import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):

    def test_min_coins_zero(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 0), 0)

    def test_min_coins_one(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 1), 1)

    def test_min_coins_two(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 2), 1)

    def test_min_coins_three(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 3), 1)

    def test_min_coins_four(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 4), 2)

    def test_min_coins_five(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 5), 2)

    def test_min_coins_six(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 6), 2)

    def test_min_coins_seven(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 7), 3)

    def test_min_coins_eight(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 8), 3)

    def test_min_coins_nine(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 9), 3)

    def test_min_coins_ten(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 10), 3)
