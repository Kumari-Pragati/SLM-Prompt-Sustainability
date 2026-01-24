import unittest
from mbpp_687_code import recur_gcd

class TestRecurGcd(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(recur_gcd(48, 18), 6)

    def test_boundary_conditions(self):
        self.assertEqual(recur_gcd(0, 18), 18)
        self.assertEqual(recur_gcd(18, 0), 18)
        self.assertEqual(recur_gcd(1, 1), 1)

    def test_edge_conditions(self):
        self.assertEqual(recur_gcd(18, 1), 1)
        self.assertEqual(recur_gcd(1, 18), 1)
        self.assertEqual(recur_gcd(0, 1), 1)
        self.assertEqual(recur_gcd(1, 0), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            recur_gcd("18", 18)
        with self.assertRaises(TypeError):
            recur_gcd(18, "18")
        with self.assertRaises(TypeError):
            recur_gcd("18", "18")
