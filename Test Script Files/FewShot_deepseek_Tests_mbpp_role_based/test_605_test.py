import unittest
from mbpp_605_code import prime_num

class TestPrimeNum(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(prime_num(5))

    def test_non_prime_number(self):
        self.assertFalse(prime_num(4))

    def test_negative_number(self):
        self.assertFalse(prime_num(-5))

    def test_zero(self):
        self.assertFalse(prime_num(0))

    def test_one(self):
        self.assertFalse(prime_num(1))

    def test_large_prime_number(self):
        self.assertTrue(prime_num(10007))
