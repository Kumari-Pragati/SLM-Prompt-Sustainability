import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_boundary_conditions(self):
        self.assertEqual(gcd(0, 18), 18)
        self.assertEqual(gcd(18, 0), 18)
        self.assertEqual(gcd(0, 0), 1)

    def test_edge_conditions(self):
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(2, 1), 1)
        self.assertEqual(gcd(1, 2), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            gcd("18", 18)
        with self.assertRaises(TypeError):
            gcd(18, "18")
        with self.assertRaises(TypeError):
            gcd("18", "18")
