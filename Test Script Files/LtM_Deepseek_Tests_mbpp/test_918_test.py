import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(coin_change([1, 2, 3], 3, 4), 4)
        self.assertEqual(coin_change([2, 5, 3], 3, 10), 5)

    def test_edge_conditions(self):
        self.assertEqual(coin_change([1], 1, 0), 1)
        self.assertEqual(coin_change([], 0, 10), 0)
        self.assertEqual(coin_change([1, 2, 5], 3, 0), 1)

    def test_boundary_conditions(self):
        self.assertEqual(coin_change([1, 2, 5], 3, 100), 24)
        self.assertEqual(coin_change([2, 5, 3], 3, 1000), 201)

    def test_complex_cases(self):
        self.assertEqual(coin_change([1, 2, 5], 3, 1000), 2001)
        self.assertEqual(coin_change([1, 2, 5], 3, 2000), 4001)
