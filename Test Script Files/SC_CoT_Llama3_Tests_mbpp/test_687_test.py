import unittest
from mbpp_687_code import recur_gcd

class TestRecurGCD(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(recur_gcd(12, 15), 3)
        self.assertEqual(recur_gcd(48, 18), 6)
        self.assertEqual(recur_gcd(24, 30), 6)

    def test_edge_cases(self):
        self.assertEqual(recur_gcd(0, 15), 15)
        self.assertEqual(recur_gcd(15, 0), 15)
        self.assertEqual(recur_gcd(1, 1), 1)

    def test_boundary_cases(self):
        self.assertEqual(recur_gcd(10, 20), 10)
        self.assertEqual(recur_gcd(20, 10), 10)
        self.assertEqual(recur_gcd(15, 15), 15)

    def test_special_cases(self):
        self.assertEqual(recur_gcd(36, 12), 12)
        self.assertEqual(recur_gcd(48, 24), 12)
        self.assertEqual(recur_gcd(24, 48), 12)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            recur_gcd('a', 15)
        with self.assertRaises(TypeError):
            recur_gcd(15, 'b')
