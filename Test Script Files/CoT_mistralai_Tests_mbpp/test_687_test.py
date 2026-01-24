import unittest
from mbpp_687_code import divmod
from 687_code import recur_gcd

class TestRecurGCD(unittest.TestCase):
    def test_gcd_positive_numbers(self):
        for a, b in [(1, 1), (1, 2), (2, 1), (2, 3), (3, 2), (4, 3), (3, 4), (5, 15), (15, 5)]:
            self.assertEqual(recur_gcd(a, b), divmod(a, b)[0])

    def test_gcd_zero(self):
        self.assertEqual(recur_gcd(0, 4), 4)
        self.assertEqual(recur_gcd(4, 0), 4)

    def test_gcd_negative_numbers(self):
        for a, b in [(-1, -1), (-1, 1), (1, -1), (-2, -3), (-3, -2), (-4, -3), (-3, -4), (-5, 15), (-15, 5)]:
            self.assertEqual(recur_gcd(a, b), divmod(-a, b)[0])

    def test_gcd_one(self):
        self.assertEqual(recur_gcd(1, 1), 1)
        self.assertEqual(recur_gcd(1, 2), 1)
        self.assertEqual(recur_gcd(2, 1), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, recur_gcd, 0.0, 1)
        self.assertRaises(TypeError, recur_gcd, 'a', 1)
