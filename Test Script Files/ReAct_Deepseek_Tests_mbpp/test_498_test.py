import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(101, 1), 1)
        self.assertEqual(gcd(15, 25), 5)

    def test_edge_cases(self):
        self.assertEqual(gcd(0, 18), 18)
        self.assertEqual(gcd(101, 0), 101)
        self.assertEqual(gcd(0, 0), 0)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            gcd("15", 25)
        with self.assertRaises(TypeError):
            gcd(15, "25")
        with self.assertRaises(TypeError):
            gcd("15", "25")
