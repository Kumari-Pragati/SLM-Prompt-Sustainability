import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):
    def test_perfect_square(self):
        self.assertEqual(count_Divisors(4), 2)
        self.assertEqual(count_Divisors(9), 4)
        self.assertEqual(count_Divisors(16), 4)
        self.assertEqual(count_Divisors(25), 6)

    def test_prime_number(self):
        self.assertEqual(count_Divisors(2), 1)
        self.assertEqual(count_Divisors(3), 2)
        self.assertEqual(count_Divisors(5), 2)
        self.assertEqual(count_Divisors(7), 2)

    def test_composite_number(self):
        self.assertEqual(count_Divisors(6), 4)
        self.assertEqual(count_Divisors(10), 4)
        self.assertEqual(count_Divisors(12), 6)
        self.assertEqual(count_Divisors(15), 6)

    def test_zero(self):
        self.assertEqual(count_Divisors(0), 0)

    def test_negative_number(self):
        self.assertEqual(count_Divisors(-1), 1)
