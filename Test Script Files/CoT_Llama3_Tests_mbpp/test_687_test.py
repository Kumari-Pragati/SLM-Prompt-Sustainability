import unittest
from mbpp_687_code import recur_gcd

class TestRecurGcd(unittest.TestCase):

    def test_recur_gcd_typical(self):
        self.assertEqual(recur_gcd(12, 15), 3)

    def test_recur_gcd_zero(self):
        self.assertEqual(recur_gcd(0, 15), 15)

    def test_recur_gcd_one(self):
        self.assertEqual(recur_gcd(1, 15), 1)

    def test_recur_gcd_edge(self):
        self.assertEqual(recur_gcd(15, 0), 15)

    def test_recur_gcd_negative(self):
        self.assertEqual(recur_gcd(-12, 15), 3)

    def test_recur_gcd_negative_edge(self):
        self.assertEqual(recur_gcd(-12, 0), 12)

    def test_recur_gcd_invalid_input(self):
        with self.assertRaises(TypeError):
            recur_gcd('a', 15)
