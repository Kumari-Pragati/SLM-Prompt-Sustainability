import unittest
from mbpp_687_code import recur_gcd

class TestRecurGcd(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(recur_gcd(12, 15), 3)
        self.assertEqual(recur_gcd(24, 30), 6)
        self.assertEqual(recur_gcd(48, 60), 12)

    def test_edge_cases(self):
        self.assertEqual(recur_gcd(0, 15), 15)
        self.assertEqual(recur_gcd(15, 0), 15)
        self.assertEqual(recur_gcd(1, 1), 1)
        self.assertEqual(recur_gcd(1, 0), 1)

    def test_boundary_cases(self):
        self.assertEqual(recur_gcd(12, 12), 12)
        self.assertEqual(recur_gcd(24, 24), 24)
        self.assertEqual(recur_gcd(48, 48), 48)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            recur_gcd('a', 15)
        with self.assertRaises(TypeError):
            recur_gcd(15, 'b')
