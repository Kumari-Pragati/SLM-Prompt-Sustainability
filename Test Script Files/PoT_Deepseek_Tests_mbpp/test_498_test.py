import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(gcd(10, 5), 5)
        self.assertEqual(gcd(21, 14), 7)
        self.assertEqual(gcd(36, 48), 12)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(10, 0), 10)
        self.assertEqual(gcd(0, 0), 1)

    def test_invalid_or_exceptional_inputs(self):
        with self.assertRaises(TypeError):
            gcd("10", 5)
        with self.assertRaises(TypeError):
            gcd(10, "5")
        with self.assertRaises(TypeError):
            gcd("10", "5")
