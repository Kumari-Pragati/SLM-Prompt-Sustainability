import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):
    def test_count_divisors_positive_integer(self):
        self.assertEqual(count_Divisors(4), "Even")
        self.assertEqual(count_Divisors(6), "Even")
        self.assertEqual(count_Divisors(25), "Odd")
        self.assertEqual(count_Divisors(28), "Even")

    def test_count_divisors_zero(self):
        self.assertEqual(count_Divisors(0), "Odd")

    def test_count_divisors_negative_integer(self):
        self.assertEqual(count_Divisors(-4), "Even")

    def test_count_divisors_one(self):
        self.assertEqual(count_Divisors(1), "Odd")

    def test_count_divisors_large_integer(self):
        self.assertEqual(count_Divisors(1000000), "Even")

    def test_count_divisors_fraction(self):
        self.assertRaises(TypeError, count_Divisors, 3.14)

    def test_count_divisors_complex_number(self):
        self.assertRaises(TypeError, count_Divisors, 3j)
