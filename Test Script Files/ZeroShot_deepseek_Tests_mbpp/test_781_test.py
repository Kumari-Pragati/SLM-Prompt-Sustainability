import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):

    def test_count_Divisors_even(self):
        self.assertEqual(count_Divisors(10), "Even")
        self.assertEqual(count_Divisors(24), "Even")
        self.assertEqual(count_Divisors(100), "Even")

    def test_count_Divisors_odd(self):
        self.assertEqual(count_Divisors(15), "Odd")
        self.assertEqual(count_Divisors(25), "Odd")
        self.assertEqual(count_Divisors(101), "Odd")

    def test_count_Divisors_zero(self):
        self.assertEqual(count_Divisors(0), "Even")

    def test_count_Divisors_negative(self):
        self.assertEqual(count_Divisors(-10), "Even")
        self.assertEqual(count_Divisors(-25), "Odd")
