import unittest
from mbpp_45_code import get_gcd

class TestGetGCD(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(get_gcd([48, 18]), 6)

    def test_single_number(self):
        self.assertEqual(get_gcd([48]), 48)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            get_gcd([])

    def test_negative_numbers(self):
        self.assertEqual(get_gcd([-48, -18]), 6)

    def test_zero(self):
        self.assertEqual(get_gcd([0, 18]), 18)

    def test_large_numbers(self):
        self.assertEqual(get_gcd([1000000000, 2000000000]), 1000000000)

    def test_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            get_gcd([48.5, 18])

    def test_non_integer_list(self):
        with self.assertRaises(TypeError):
            get_gcd(['48', 18])
