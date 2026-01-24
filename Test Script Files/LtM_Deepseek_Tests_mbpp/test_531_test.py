import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(min_coins([1, 2, 5], 3, 11), 3)
        self.assertEqual(min_coins([1, 2, 5], 3, 0), 0)

    def test_edge_conditions(self):
        self.assertEqual(min_coins([], 0, 10), 0)
        self.assertEqual(min_coins([1, 2, 5], 3, -1), 0)
        self.assertEqual(min_coins([1, 2, 5], 3, sys.maxsize), sys.maxsize)

    def test_boundary_conditions(self):
        self.assertEqual(min_coins([1, 2, 5], 3, 1), 1)
        self.assertEqual(min_coins([1, 2, 5], 3, 2), 1)
        self.assertEqual(min_coins([1, 2, 5], 3, 5), 1)
        self.assertEqual(min_coins([1, 2, 5], 3, 6), 2)
        self.assertEqual(min_coins([1, 2, 5], 3, 7), 2)
        self.assertEqual(min_coins([1, 2, 5], 3, 8), 2)
        self.assertEqual(min_coins([1, 2, 5], 3, 9), 2)
        self.assertEqual(min_coins([1, 2, 5], 3, 10), 2)

    def test_complex_cases(self):
        self.assertEqual(min_coins([1, 2, 5], 3, 15), 3)
        self.assertEqual(min_coins([1, 2, 5], 3, 20), 4)
        self.assertEqual(min_coins([1, 2, 5], 3, 25), 5)
