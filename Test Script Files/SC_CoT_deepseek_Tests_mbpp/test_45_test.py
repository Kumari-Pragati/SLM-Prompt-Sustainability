import unittest
from mbpp_45_code import get_gcd

class TestGetGcd(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_gcd([48, 18]), 6)

    def test_edge_case(self):
        self.assertEqual(get_gcd([1, 1]), 1)

    def test_boundary_case(self):
        self.assertEqual(get_gcd([0, 18]), 18)
        self.assertEqual(get_gcd([48, 0]), 48)

    def test_special_case(self):
        self.assertEqual(get_gcd([101, 103]), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_gcd("18, 24")
        with self.assertRaises(TypeError):
            get_gcd([18, "24"])
        with self.assertRaises(TypeError):
            get_gcd([18, 24, "30"])
        with self.assertRaises(TypeError):
            get_gcd([18, 24, 30, 36, "42"])
        with self.assertRaises(ValueError):
            get_gcd([])
        with self.assertRaises(ValueError):
            get_gcd([18])
