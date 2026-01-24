import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):

    def test_zero(self):
        """Test with zero"""
        self.assertEqual(count_Primes_nums(0), 0)

    def test_one(self):
        """Test with one"""
        self.assertEqual(count_Primes_nums(1), 0)

    def test_two(self):
        """Test with two"""
        self.assertEqual(count_Primes_nums(2), 1)

    def test_small_positive_numbers(self):
        """Test with small positive numbers"""
        for num in range(3, 11):
            self.assertEqual(count_Primes_nums(num), num - 1)

    def test_large_positive_numbers(self):
        """Test with large positive numbers"""
        for num in range(100, 1000, 100):
            self.assertEqual(count_Primes_nums(num), self.approx_primes(num))

    def test_negative_numbers(self):
        """Test with negative numbers"""
        for num in range(-10, 0, -1):
            with self.assertRaises(ValueError):
                count_Primes_nums(num)

    def test_large_negative_numbers(self):
        """Test with large negative numbers"""
        for num in range(-1000, -100, -100):
            with self.assertRaises(ValueError):
                count_Primes_nums(num)

    def approx_primes(self, n):
        """Helper function to approximate the number of primes less than n"""
        return (n // 2) * (n // 3) // 2 + n // 6
