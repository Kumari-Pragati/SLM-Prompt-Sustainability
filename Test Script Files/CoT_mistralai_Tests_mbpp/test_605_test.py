import unittest
from mbpp_605_code import prime_num

class TestPrimeNum(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(prime_num(2))
        self.assertTrue(prime_num(3))
        self.assertTrue(prime_num(5))
        self.assertTrue(prime_num(7))

    def test_non_prime_numbers(self):
        self.assertFalse(prime_num(4))
        self.assertFalse(prime_num(6))
        self.assertFalse(prime_num(8))
        self.assertFalse(prime_num(9))

    def test_large_prime_numbers(self):
        self.assertTrue(prime_num(11))
        self.assertTrue(prime_num(13))
        self.assertTrue(prime_num(17))
        self.assertTrue(prime_num(19))

    def test_zero_and_negative_numbers(self):
        self.assertFalse(prime_num(0))
        self.assertFalse(prime_num(-1))
        self.assertFalse(prime_num(-2))
