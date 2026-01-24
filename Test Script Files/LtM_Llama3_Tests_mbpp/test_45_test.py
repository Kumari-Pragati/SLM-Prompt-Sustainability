import unittest
from mbpp_45_code import get_gcd

class TestGetGcd(unittest.TestCase):
    def test_simple_gcd(self):
        self.assertEqual(get_gcd([2, 3]), 1)
        self.assertEqual(get_gcd([4, 6]), 2)
        self.assertEqual(get_gcd([10, 15]), 5)

    def test_gcd_with_zero(self):
        self.assertEqual(get_gcd([0, 3]), 3)
        self.assertEqual(get_gcd([4, 0]), 4)

    def test_gcd_with_negative(self):
        self.assertEqual(get_gcd([-2, 3]), 1)
        self.assertEqual(get_gcd([4, -6]), 2)

    def test_gcd_with_multiple_numbers(self):
        self.assertEqual(get_gcd([2, 3, 4, 6]), 1)
        self.assertEqual(get_gcd([10, 15, 20, 30]), 5)

    def test_gcd_with_empty_input(self):
        with self.assertRaises(IndexError):
            get_gcd([])

    def test_gcd_with_single_input(self):
        with self.assertRaises(IndexError):
            get_gcd([1])
