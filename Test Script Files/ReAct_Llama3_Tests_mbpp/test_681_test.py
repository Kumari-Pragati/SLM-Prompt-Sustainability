import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual(smallest_Divisor(4), 2)

    def test_odd_numbers(self):
        self.assertEqual(smallest_Divisor(5), 5)

    def test_prime_numbers(self):
        self.assertEqual(smallest_Divisor(7), 7)

    def test_perfect_squares(self):
        self.assertEqual(smallest_Divisor(9), 3)

    def test_perfect_cubes(self):
        self.assertEqual(smallest_Divisor(27), 3)

    def test_large_numbers(self):
        self.assertEqual(smallest_Divisor(100), 2)

    def test_single_digit_numbers(self):
        self.assertEqual(smallest_Divisor(1), 1)

    def test_zero(self):
        with self.assertRaises(ValueError):
            smallest_Divisor(0)
