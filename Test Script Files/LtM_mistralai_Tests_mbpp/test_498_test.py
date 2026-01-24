import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(gcd(36, 18), 6)
        self.assertEqual(gcd(25, 10), 5)
        self.assertEqual(gcd(12, 18), 6)

    def test_edge_and_boundary(self):
        self.assertEqual(gcd(0, 16), 16)
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(10**10, 1), 1)
        self.assertEqual(gcd(1, 10**10), 1)
        self.assertEqual(gcd(-10, 10), 10)
        self.assertEqual(gcd(10, -10), 10)

    def test_complex(self):
        self.assertEqual(gcd(20*33*55, 20*33*55*77), 77)
        self.assertEqual(gcd(2**63, 3**63), 3**63)
        self.assertEqual(gcd(2**63, 2**63 + 1), 1)
