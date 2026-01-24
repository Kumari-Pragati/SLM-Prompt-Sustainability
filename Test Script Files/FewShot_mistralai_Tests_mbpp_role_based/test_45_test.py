import unittest
from mbpp_45_code import get_gcd

class TestGetGCD(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(get_gcd([12, 16]), 4)
        self.assertEqual(get_gcd([24, 18]), 6)
        self.assertEqual(get_gcd([36, 24]), 12)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_gcd([0, 0]), 0)
        self.assertEqual(get_gcd([1, 1]), 1)
        self.assertEqual(get_gcd([1, 0]), 0)
        self.assertEqual(get_gcd([-1, -1]), 1)
        self.assertEqual(get_gcd([-1, 1]), 1)
        self.assertEqual(get_gcd([1, -1]), 1)
        self.assertEqual(get_gcd([0, 1]), 0)
        self.assertEqual(get_gcd([1, 0]), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, get_gcd, [1, 'a'])
        self.assertRaises(TypeError, get_gcd, ['a', 1])
        self.assertRaises(TypeError, get_gcd, [1])
        self.assertRaises(TypeError, get_gcd, [])
