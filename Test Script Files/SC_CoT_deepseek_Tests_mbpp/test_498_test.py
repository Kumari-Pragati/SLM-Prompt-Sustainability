import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):
    
    def test_typical_inputs(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(101, 103), 1)
        self.assertEqual(gcd(36, 60), 12)

    def test_boundary_conditions(self):
        self.assertEqual(gcd(0, 18), 18)
        self.assertEqual(gcd(18, 0), 18)
        self.assertEqual(gcd(0, 0), 1)

    def test_edge_cases(self):
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(2, 1), 1)
        self.assertEqual(gcd(1, 2), 1)

    def test_special_cases(self):
        self.assertEqual(gcd(10, 10), 10)
        self.assertEqual(gcd(100, 200), 100)
        self.assertEqual(gcd(1000, 1000), 1000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            gcd("18", 18)
        with self.assertRaises(TypeError):
            gcd(18, "18")
        with self.assertRaises(TypeError):
            gcd("18", "18")
