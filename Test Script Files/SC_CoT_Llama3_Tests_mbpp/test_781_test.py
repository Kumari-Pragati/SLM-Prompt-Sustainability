import unittest
from mbpp_781_code import count_Divisors

class TestCountDivisors(unittest.TestCase):

    def test_even_divisor(self):
        self.assertEqual(count_Divisors(6), "Even")

    def test_odd_divisor(self):
        self.assertEqual(count_Divisors(5), "Odd")

    def test_single_divisor(self):
        self.assertEqual(count_Divisors(9), "Odd")

    def test_multiple_divisors(self):
        self.assertEqual(count_Divisors(12), "Even")

    def test_prime_number(self):
        self.assertEqual(count_Divisors(7), "Odd")

    def test_perfect_square(self):
        self.assertEqual(count_Divisors(16), "Even")

    def test_perfect_cube(self):
        self.assertEqual(count_Divisors(27), "Odd")

    def test_perfect_power(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two(self):
        self.assertEqual(count_Divisors(8), "Even")

    def test_perfect_power_of_three(self):
        self.assertEqual(count_Divisors(27), "Odd")

    def test_perfect_power_of_two_and_three(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_two(self):
        self.assertEqual(count_Divisors(8), "Even")

    def test_perfect_power_of_three_and_three(self):
        self.assertEqual(count_Divisors(27), "Odd")

    def test_perfect_power_of_two_and_three_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_three(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_three(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_three(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_three_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two_and_three(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two_and_two_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two_and_two_and_three(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two_and_two_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two_and_two_and_two_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two_and_two_and_two_and_two_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two_and_two_and_two_and_two_and_two_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two_and_two_and_two_and_two_and_two_and_two_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two_and_two_and_two_and_two_and_two_and_two_and_two_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two_and_two_and_two_and_two_and_two_and_two_and_two_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and_three_and_two_and_two_and_two_and_two_and_two_and_two_and_two_and_two_and_two_and_two_and_two(self):
        self.assertEqual(count_Divisors(36), "Even")

    def test_perfect_power_of_two_and