import unittest
from mbpp_45_code import get_gcd

class TestGetGCD(unittest.TestCase):

    def test_get_gcd_two_numbers(self):
        self.assertEqual(get_gcd([12, 18]), 6)
        self.assertEqual(get_gcd([25, 10]), 5)
        self.assertEqual(get_gcd([49, 22]), 7)

    def test_get_gcd_three_numbers(self):
        self.assertEqual(get_gcd([12, 18, 6]), 6)
        self.assertEqual(get_gcd([25, 10, 5]), 5)
        self.assertEqual(get_gcd([49, 22, 7]), 7)

    def test_get_gcd_four_numbers(self):
        self.assertEqual(get_gcd([12, 18, 6, 3]), 3)
        self.assertEqual(get_gcd([25, 10, 5, 2]), 1)
        self.assertEqual(get_gcd([49, 22, 7, 11]), 1)
