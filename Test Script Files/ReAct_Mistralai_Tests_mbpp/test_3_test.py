import unittest
from mbpp_3_code import is_not_prime

class TestIsNotPrime(unittest.TestCase):

    def test_prime_numbers(self):
        """Test that non-prime numbers are correctly identified"""
        self.assertFalse(is_not_prime(2))
        self.assertFalse(is_not_prime(3))
        self.assertFalse(is_not_prime(5))
        self.assertFalse(is_not_prime(7))

    def test_composite_numbers(self):
        """Test that composite numbers are correctly identified"""
        self.assertTrue(is_not_prime(4))
        self.assertTrue(is_not_prime(6))
        self.assertTrue(is_not_prime(9))
        self.assertTrue(is_not_prime(10))

    def test_edge_cases(self):
        """Test edge cases for the function"""
        self.assertFalse(is_not_prime(1))  # Not a number
        self.assertTrue(is_not_prime(0))  # Zero
        self.assertFalse(is_not_prime(2))  # Prime number
        self.assertTrue(is_not_prime(math.isqrt(1000) + 1))  # Large number
