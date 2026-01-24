import unittest
from mbpp_45_code import get_gcd

class TestGetGCD(unittest.TestCase):

    def test_get_gcd(self):
        self.assertEqual(get_gcd([2, 4, 6]), 2)
        self.assertEqual(get_gcd([12, 15, 18]), 3)
        self.assertEqual(get_gcd([10, 20, 30]), 10)
        self.assertEqual(get_gcd([5, 15, 25]), 5)
        self.assertEqual(get_gcd([7, 21, 35]), 7)
        self.assertEqual(get_gcd([1, 2, 3, 4, 5]), 1)
        self.assertEqual(get_gcd([10, 20, 30, 40, 50]), 10)
        self.assertEqual(get_gcd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(get_gcd([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 2)
        self.assertEqual(get_gcd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 1)
