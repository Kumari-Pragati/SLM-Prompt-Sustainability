import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):
    def test_even_divisors(self):
        self.assertEqual(count_Divisors(12), "Even")

    def test_odd_divisors(self):
        self.assertEqual(count_Divisors(15), "Odd")

    def test_prime_number(self):
        self.assertEqual(count_Divisors(7), "Odd")

    def test_perfect_square(self):
        self.assertEqual(count_Divisors(16), "Even")

    def test_perfect_cube(self):
        self.assertEqual(count_Divisors(27), "Odd")

    def test_large_number(self):
        self.assertEqual(count_Divisors(1000), "Odd")

    def test_zero(self):
        self.assertEqual(count_Divisors(0), "Even")

    def test_negative_number(self):
        with self.assertRaises(TypeError):
            count_Divisors(-1)
