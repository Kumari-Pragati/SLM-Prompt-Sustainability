import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):
    def test_gcd_simple(self):
        self.assertEqual(gcd(4, 6), 2)
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(24, 30), 6)

    def test_gcd_edge(self):
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(10, 0), 10)
        self.assertEqual(gcd(0, 10), 10)

    def test_gcd_invalid(self):
        with self.assertRaises(TypeError):
            gcd('a', 5)
        with self.assertRaises(TypeError):
            gcd(5, 'b')
