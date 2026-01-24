import unittest
from mbpp_687_code import recur_gcd

class TestRecurGCD(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(recur_gcd(4, 2), 2)
        self.assertEqual(recur_gcd(8, 4), 4)
        self.assertEqual(recur_gcd(12, 16), 4)

    def test_edge_inputs(self):
        self.assertEqual(recur_gcd(0, 1), 1)
        self.assertEqual(recur_gcd(1, 0), 1)
        self.assertEqual(recur_gcd(1, 1), 1)
        self.assertEqual(recur_gcd(-1, 1), 1)
        self.assertEqual(recur_gcd(1, -1), 1)

    def test_boundary_inputs(self):
        self.assertEqual(recur_gcd(2**31, 1), 1)
        self.assertEqual(recur_gcd(1, 2**31), 1)
        self.assertEqual(recur_gcd(-2**31, 1), 1)
        self.assertEqual(recur_gcd(1, -2**31), 1)

    def test_complex_inputs(self):
        self.assertEqual(recur_gcd(17, 29), 1)
        self.assertEqual(recur_gcd(100, 200), 100)
        self.assertEqual(recur_gcd(1000000007, 2000000007), 1)
