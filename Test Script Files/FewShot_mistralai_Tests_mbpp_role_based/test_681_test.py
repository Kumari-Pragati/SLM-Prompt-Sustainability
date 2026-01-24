import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):
    def test_positive_even(self):
        self.assertEqual(smallest_Divisor(16), 4)

    def test_positive_odd(self):
        self.assertEqual(smallest_Divisor(15), 3)

    def test_zero(self):
        self.assertEqual(smallest_Divisor(0), 0)

    def test_negative_number(self):
        self.assertEqual(smallest_Divisor(-1), -1)

    def test_one(self):
        self.assertEqual(smallest_Divisor(1), 1)

    def test_large_prime_number(self):
        self.assertEqual(smallest_Divisor(101), 101)
