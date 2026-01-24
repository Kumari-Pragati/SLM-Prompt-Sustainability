import unittest
from mbpp_681_code import smallest_Divisor

class TestSmallestDivisor(unittest.TestCase):
    def test_even_number(self):
        self.assertEqual(smallest_Divisor(4), 2)

    def test_odd_number(self):
        self.assertEqual(smallest_Divisor(5), 5)

    def test_prime_number(self):
        self.assertEqual(smallest_Divisor(7), 7)

    def test_power_of_two(self):
        self.assertEqual(smallest_Divisor(8), 2)

    def test_power_of_three(self):
        self.assertEqual(smallest_Divisor(27), 3)

    def test_large_number(self):
        self.assertEqual(smallest_Divisor(100), 2)

    def test_one(self):
        self.assertEqual(smallest_Divisor(1), 1)
