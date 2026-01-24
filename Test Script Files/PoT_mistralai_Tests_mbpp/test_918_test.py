import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(coin_change([1, 2, 5], 11, 3), [1, 1, 1, 1, 1, 2, 5])
        self.assertEqual(coin_change([2], 3, 1), [1])
        self.assertEqual(coin_change([1], 4, 1), [1, 1, 1, 1])

    def test_edge_and_boundary_cases(self):
        self.assertEqual(coin_change([1], 0, 0), [])
        self.assertEqual(coin_change([1], 1, 0), [1])
        self.assertEqual(coin_change([1], 2, 0), [1, 1])
        self.assertEqual(coin_change([1], 3, 0), [1, 1, 1])
        self.assertEqual(coin_change([1], 4, 0), [1, 1, 1, 1])

        self.assertEqual(coin_change([1], 1, 1), [1])
        self.assertEqual(coin_change([1], 2, 1), [1, 1])
        self.assertEqual(coin_change([1], 3, 1), [1, 1, 1])
        self.assertEqual(coin_change([1], 4, 1), [1, 1, 1, 1])

        self.assertEqual(coin_change([1, 2], 3, 1), [2])
        self.assertEqual(coin_change([1, 2], 4, 1), [1, 2])
        self.assertEqual(coin_change([1, 2], 5, 1), [1, 1, 2])
        self.assertEqual(coin_change([1, 2], 6, 1), [1, 2, 2])
        self.assertEqual(coin_change([1, 2], 7, 1), [1, 1, 2, 2])

        self.assertEqual(coin_change([1, 2], 3, 2), [1, 2])
        self.assertEqual(coin_change([1, 2], 4, 2), [1, 1, 2])
        self.assertEqual(coin_change([1, 2], 5, 2), [1, 2, 2])
        self.assertEqual(coin_change([1, 2], 6, 2), [1, 1, 1, 2])
        self.assertEqual(coin_change([1, 2], 7, 2), [1, 2, 2, 2])

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, coin_change, [], 11, 3)
        self.assertRaises(ValueError, coin_change, [1], 11, 0)
        self.assertRaises(ValueError, coin_change, [1], 11, -1)
