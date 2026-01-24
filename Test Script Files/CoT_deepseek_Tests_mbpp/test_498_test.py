import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_typical_case_2(self):
        self.assertEqual(gcd(101, 103), 1)

    def test_boundary_case(self):
        self.assertEqual(gcd(0, 18), 18)
        self.assertEqual(gcd(18, 0), 18)
        self.assertEqual(gcd(0, 0), 0)

    def test_edge_case(self):
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(18, 1), 1)
        self.assertEqual(gcd(1, 18), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            gcd("18", 18)
        with self.assertRaises(TypeError):
            gcd(18, "18")
        with self.assertRaises(TypeError):
            gcd("18", "18")
