import unittest
from mbpp_45_code import get_gcd

class TestGetGCD(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(get_gcd([12, 16]), 4)
        self.assertEqual(get_gcd([36, 24]), 12)
        self.assertEqual(get_gcd([10, 2]), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_gcd([0, 10]), 10)
        self.assertEqual(get_gcd([10, 0]), 10)
        self.assertEqual(get_gcd([1, 1]), 1)
        self.assertEqual(get_gcd([-10, 10]), 10)
        self.assertEqual(get_gcd([10, -10]), 10)
        self.assertEqual(get_gcd([10, 0]), 10)
        self.assertEqual(get_gcd([0, 10]), 10)

    def test_negative_numbers(self):
        self.assertEqual(get_gcd([-12, -16]), 4)
        self.assertEqual(get_gcd([-36, -24]), 12)
        self.assertEqual(get_gcd([-10, -2]), 2)

    def test_single_number(self):
        self.assertEqual(get_gcd([10]), 10)

    def test_empty_list(self):
        self.assertRaises(ValueError, get_gcd, [])
