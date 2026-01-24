import unittest
from mbpp_605_code import prime_num

class TestPrimeNum(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(prime_num(2))
        self.assertTrue(prime_num(3))
        self.assertTrue(prime_num(5))
        self.assertTrue(prime_num(7))

    def test_composite_numbers(self):
        self.assertFalse(prime_num(4))
        self.assertFalse(prime_num(6))
        self.assertFalse(prime_num(8))
        self.assertFalse(prime_num(9))

    def test_edge_cases(self):
        self.assertTrue(prime_num(0))  # Edge case: non-positive number
        self.assertFalse(prime_num(1))  # Edge case: number 1
        self.assertTrue(prime_num(2**64 - 1))  # Edge case: largest prime number
