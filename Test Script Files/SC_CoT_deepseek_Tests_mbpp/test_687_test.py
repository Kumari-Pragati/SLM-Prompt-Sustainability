import unittest
from mbpp_687_code import recur_gcd

class TestRecurGcd(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(recur_gcd(48, 18), 6)
        self.assertEqual(recur_gcd(101, 103), 1)

    def test_boundary_conditions(self):
        self.assertEqual(recur_gcd(0, 10), 10)
        self.assertEqual(recur_gcd(10, 0), 10)
        self.assertEqual(recur_gcd(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(recur_gcd(1, 1), 1)
        self.assertEqual(recur_gcd(1, 100), 1)
        self.assertEqual(recur_gcd(100, 1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            recur_gcd("10", 10)
        with self.assertRaises(TypeError):
            recur_gcd(10, "10")
        with self.assertRaises(TypeError):
            recur_gcd("10", "10")
        with self.assertRaises(ValueError):
            recur_gcd(-10, 10)
        with self.assertRaises(ValueError):
            recur_gcd(10, -10)
        with self.assertRaises(ValueError):
            recur_gcd(-10, -10)
