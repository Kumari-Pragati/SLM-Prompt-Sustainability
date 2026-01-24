import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):

    def test_count_Divisors_even(self):
        self.assertEqual(count_Divisors(10), "Even")

    def test_count_Divisors_odd(self):
        self.assertEqual(count_Divisors(11), "Odd")

    def test_count_Divisors_zero(self):
        self.assertEqual(count_Divisors(0), "Even")

    def test_count_Divisors_negative(self):
        with self.assertRaises(ValueError):
            count_Divisors(-1)

    def test_count_Divisors_non_integer(self):
        with self.assertRaises(TypeError):
            count_Divisors(10.5)
