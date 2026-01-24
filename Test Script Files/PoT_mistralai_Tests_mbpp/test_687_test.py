import unittest
from mbpp_687_code import recur_gcd

class TestRecurGCD(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(recur_gcd(36, 24), 12)
        self.assertEqual(recur_gcd(48, 18), 6)
        self.assertEqual(recur_gcd(10, 20), 10)
        self.assertEqual(recur_gcd(25, 10), 5)
        self.assertEqual(recur_gcd(125, 100), 25)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(recur_gcd(0, 1), 1)
        self.assertEqual(recur_gcd(1, 0), 1)
        self.assertEqual(recur_gcd(1, 1), 1)
        self.assertEqual(recur_gcd(-1, 1), 1)
        self.assertEqual(recur_gcd(1, -1), 1)
        self.assertEqual(recur_gcd(1, 0), 1)
        self.assertEqual(recur_gcd(0, 0), 0)
