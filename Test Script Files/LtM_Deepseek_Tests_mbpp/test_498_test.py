import unittest
from mbpp_498_code import gcd

class TestGCD(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(gcd(10, 2), 2)
        self.assertEqual(gcd(15, 5), 5)
        self.assertEqual(gcd(21, 7), 7)

    def test_edge_conditions(self):
        self.assertEqual(gcd(0, 1), 1)
        self.assertEqual(gcd(1, 0), 1)
        self.assertEqual(gcd(0, 0), 1)

    def test_boundary_conditions(self):
        self.assertEqual(gcd(2**31-1, 2**31-1), 2**31-1)
        self.assertEqual(gcd(2**31-1, 0), 2**31-1)
        self.assertEqual(gcd(0, 2**31-1), 2**31-1)

    def test_complex_cases(self):
        self.assertEqual(gcd(101, 103), 1)
        self.assertEqual(gcd(100, 200), 100)
        self.assertEqual(gcd(1000, 2000), 1000)
