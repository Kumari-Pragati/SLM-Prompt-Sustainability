import unittest
from mbpp_605_code import prime_num

class TestPrimeNum(unittest.TestCase):

    def test_prime_num_positive(self):
        self.assertTrue(prime_num(5))

    def test_prime_num_negative(self):
        self.assertFalse(prime_num(-5))

    def test_prime_num_zero(self):
        self.assertFalse(prime_num(0))

    def test_prime_num_one(self):
        self.assertTrue(prime_num(1))

    def test_prime_num_prime(self):
        self.assertTrue(prime_num(23))

    def test_prime_num_composite(self):
        self.assertFalse(prime_num(6))

    def test_prime_num_edge(self):
        self.assertTrue(prime_num(2))
