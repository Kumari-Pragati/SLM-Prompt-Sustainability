import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):
    def test_gcd_typical(self):
        self.assertEqual(gcd(36, 21), 3)
        self.assertEqual(gcd(10, 15), 5)
        self.assertEqual(gcd(25, 10), 5)
        self.assertEqual(gcd(48, 18), 6)

    def test_gcd_edge_and_boundary(self):
        self.assertEqual(gcd(0, 0), 0)
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(1, 2), 1)
        self.assertEqual(gcd(2, 1), 1)
        self.assertEqual(gcd(-5, 5), 1)
        self.assertEqual(gcd(5, -5), 1)
        self.assertEqual(gcd(2**64, 2**64), 2**64)
        self.assertEqual(gcd(2**64 - 1, 2**64), 1)
