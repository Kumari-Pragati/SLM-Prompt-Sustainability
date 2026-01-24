import unittest
from mbpp_687_code import recur_gcd

class TestRecurGcd(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(recur_gcd(10, 5), 5)
        self.assertEqual(recur_gcd(15, 10), 5)
        self.assertEqual(recur_gcd(21, 14), 7)
        self.assertEqual(recur_gcd(36, 24), 12)

    def test_edge_cases(self):
        self.assertEqual(recur_gcd(0, 10), 10)
        self.assertEqual(recur_gcd(10, 0), 10)
        self.assertEqual(recur_gcd(0, 0), 0)
        self.assertEqual(recur_gcd(1, 1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            recur_gcd("10", 5)
        with self.assertRaises(TypeError):
            recur_gcd(10, "5")
        with self.assertRaises(TypeError):
            recur_gcd("10", "5")
        with self.assertRaises(TypeError):
            recur_gcd(10.5, 5)
        with self.assertRaises(TypeError):
            recur_gcd(10, 5.5)
        with self.assertRaises(TypeError):
            recur_gcd(10.5, 5.5)
