import unittest
from mbpp_45_code import get_gcd

class TestGetGcd(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(get_gcd([48, 18]), 6)
        self.assertEqual(get_gcd([101, 103]), 1)

    def test_edge_conditions(self):
        self.assertEqual(get_gcd([0, 18]), 18)
        self.assertEqual(get_gcd([10, 0]), 10)
        self.assertEqual(get_gcd([0, 0]), 0)

    def test_complex_cases(self):
        self.assertEqual(get_gcd([36, 12, 48]), 12)
        self.assertEqual(get_gcd([105, 210, 315]), 21)
        self.assertEqual(get_gcd([7, 21, 49, 14]), 7)
