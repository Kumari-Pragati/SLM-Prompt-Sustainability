import unittest
from mbpp_45_code import get_gcd

class TestGetGcd(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_gcd([48, 18]), 6)

    def test_boundary_condition(self):
        self.assertEqual(get_gcd([0, 18]), 18)
        self.assertEqual(get_gcd([48, 0]), 48)

    def test_edge_case(self):
        self.assertEqual(get_gcd([1, 1]), 1)
        self.assertEqual(get_gcd([100, 100]), 100)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_gcd([48, 'a'])
        with self.assertRaises(TypeError):
            get_gcd(['a', 18])
        with self.assertRaises(TypeError):
            get_gcd(['a', 'b'])
        with self.assertRaises(TypeError):
            get_gcd([1, 2, 'a'])
