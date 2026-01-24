import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(coin_change([1, 2, 5], 3, 3), [1, 1, 1])
        self.assertEqual(coin_change([2, 5], 3, 2), [1, 1])
        self.assertEqual(coin_change([1, 2, 5], 4, 3), [1, 2, 1])

    def test_edge_case(self):
        self.assertEqual(coin_change([1, 2, 5], 0, 0), [0])
        self.assertEqual(coin_change([1, 2, 5], 1, 0), [0])
        self.assertEqual(coin_change([1, 2, 5], 3, 0), [1])
        self.assertEqual(coin_change([1, 2, 5], 3, 1), [1, 1])
        self.assertEqual(coin_change([1, 2, 5], 3, 2), [1, 2])
        self.assertEqual(coin_change([1, 2, 5], 3, 3), [1, 1, 1])
        self.assertEqual(coin_change([1, 2, 5], 4, 0), [0])
        self.assertEqual(coin_change([1, 2, 5], 4, 1), [1])
        self.assertEqual(coin_change([1, 2, 5], 4, 2), [1, 1])
        self.assertEqual(coin_change([1, 2, 5], 4, 3), [1, 2])
        self.assertEqual(coin_change([1, 2, 5], 4, 4), [1, 1, 1, 1])

    def test_boundary_case(self):
        self.assertEqual(coin_change([1, 2, 5], 100, 100), [99, 99])
        self.assertEqual(coin_change([1, 2, 5], 100, 101), [99, 99, 1])
        self.assertEqual(coin_change([1, 2, 5], 100, 102), [99, 99, 1, 1])
        self.assertEqual(coin_change([1, 2, 5], 100, 103), [99, 99, 1, 1, 1])

    def test_invalid_input(self):
        self.assertRaises(ValueError, coin_change, [], 3, 3)
        self.assertRaises(ValueError, coin_change, [1], 3, 0)
        self.assertRaises(ValueError, coin_change, [1, 2, 5], 0, 3)
        self.assertRaises(ValueError, coin_change, [1, 2, 5], 3, 0)
