import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):

    def test_even_divisor_count(self):
        self.assertEqual(count_Divisors(12), "Even")

    def test_odd_divisor_count(self):
        self.assertEqual(count_Divisors(15), "Odd")

    def test_single_divisor(self):
        self.assertEqual(count_Divisors(7), "Odd")

    def test_multiple_divisors(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_prime_number(self):
        self.assertEqual(count_Divisors(23), "Odd")

    def test_perfect_square(self):
        self.assertEqual(count_Divisors(16), "Even")

    def test_perfect_cube(self):
        self.assertEqual(count_Divisors(27), "Odd")

    def test_edge_case(self):
        self.assertEqual(count_Divisors(1), "Odd")

    def test_edge_case2(self):
        self.assertEqual(count_Divisors(4), "Even")
