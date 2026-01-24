import unittest
from mbpp_45_code import get_gcd

class TestGetGCD(unittest.TestCase):

    def test_get_gcd_two_numbers(self):
        self.assertEqual(get_gcd([48, 18]), 6)
        self.assertEqual(get_gcd([101, 103]), 1)
        self.assertEqual(get_gcd([100, 100]), 100)

    def test_get_gcd_multiple_numbers(self):
        self.assertEqual(get_gcd([2, 4, 6, 8]), 2)
        self.assertEqual(get_gcd([15, 25, 35]), 5)
        self.assertEqual(get_gcd([100, 200, 300]), 100)

    def test_get_gcd_with_zero(self):
        self.assertEqual(get_gcd([0, 18]), 18)
        self.assertEqual(get_gcd([101, 0]), 101)
        self.assertEqual(get_gcd([0, 0]), 0)
