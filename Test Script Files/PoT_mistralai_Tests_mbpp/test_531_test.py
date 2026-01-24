import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(min_coins([1, 2, 5], 3, 3), 2)
        self.assertEqual(min_coins([2, 5, 3, 6], 6, 10), 4)
        self.assertEqual(min_coins([1], 1, 1), 1)
        self.assertEqual(min_coins([1, 2, 3], 3, 4), 1)
        self.assertEqual(min_coins([1, 2, 3], 4, 4), 1)
        self.assertEqual(min_coins([1, 2, 3], 4, 5), 2)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(min_coins([1, 2, 5], 3, 0), 0)
        self.assertEqual(min_coins([1, 2, 5], 3, 1), 1)
        self.assertEqual(min_coins([1, 2, 5], 3, 2), 1)
        self.assertEqual(min_coins([1, 2, 5], 3, 100), 10)
