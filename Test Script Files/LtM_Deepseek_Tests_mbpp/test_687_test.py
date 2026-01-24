import unittest
from mbpp_687_code import recur_gcd

class TestRecurGcd(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(recur_gcd(10, 5), 5)
        self.assertEqual(recur_gcd(15, 10), 5)
        self.assertEqual(recur_gcd(7, 2), 1)

    def test_edge_conditions(self):
        self.assertEqual(recur_gcd(0, 10), 10)
        self.assertEqual(recur_gcd(10, 0), 10)
        self.assertEqual(recur_gcd(0, 0), 0)
        self.assertEqual(recur_gcd(1, 1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(recur_gcd(2**31-1, 2**31-1), 2**31-1)
        self.assertEqual(recur_gcd(2**31-1, 0), 2**31-1)
        self.assertEqual(recur_gcd(0, 2**31-1), 2**31-1)

    def test_complex_cases(self):
        self.assertEqual(recur_gcd(18, 48), 6)
        self.assertEqual(recur_gcd(101, 103), 1)
        self.assertEqual(recur_gcd(1000, 2000), 1000)
