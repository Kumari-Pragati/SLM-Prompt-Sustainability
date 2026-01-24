import unittest
from mbpp_687_code import recur_gcd

class TestRecurGcd(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(recur_gcd(12, 15), 3)
        self.assertEqual(recur_gcd(24, 36), 12)
        self.assertEqual(recur_gcd(101, 103), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(recur_gcd(0, 10), 10)
        self.assertEqual(recur_gcd(10, 0), 10)
        self.assertEqual(recur_gcd(0, 0), 0)
        self.assertEqual(recur_gcd(1, 1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            recur_gcd("12", 15)
        with self.assertRaises(TypeError):
            recur_gcd(12, "15")
        with self.assertRaises(TypeError):
            recur_gcd("12", "15")
