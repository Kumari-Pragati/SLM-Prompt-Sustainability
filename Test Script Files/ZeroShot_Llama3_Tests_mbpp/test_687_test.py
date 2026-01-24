import unittest
from mbpp_687_code import recur_gcd

class TestRecGCD(unittest.TestCase):

    def test_recur_gcd(self):
        self.assertEqual(recur_gcd(12, 15), 3)
        self.assertEqual(recur_gcd(48, 18), 6)
        self.assertEqual(recur_gcd(24, 30), 6)
        self.assertEqual(recur_gcd(0, 15), 15)
        self.assertEqual(recur_gcd(1, 1), 1)
        self.assertEqual(recur_gcd(12, 12), 12)
        self.assertEqual(recur_gcd(0, 0), 0)
        self.assertEqual(recur_gcd(12, 0), 12)
        self.assertEqual(recur_gcd(0, 12), 12)
