import unittest
from mbpp_605_code import prime_num

class TestPrimeNum(unittest.TestCase):
    def test_prime_num_positive(self):
        self.assertTrue(prime_num(2))
        self.assertTrue(prime_num(3))
        self.assertTrue(prime_num(5))
        self.assertTrue(prime_num(7))
        self.assertTrue(prime_num(11))

    def test_prime_num_negative(self):
        self.assertFalse(prime_num(-1))
        self.assertFalse(prime_num(-2))
        self.assertFalse(prime_num(-3))

    def test_prime_num_zero(self):
        self.assertFalse(prime_num(0))

    def test_prime_num_one(self):
        self.assertTrue(prime_num(1))

    def test_prime_num_edge(self):
        self.assertFalse(prime_num(4))
        self.assertFalse(prime_num(6))
        self.assertFalse(prime_num(8))
        self.assertFalse(prime_num(9))
        self.assertFalse(prime_num(10))

    def test_prime_num_large(self):
        self.assertTrue(prime_num(100))
        self.assertTrue(prime_num(101))
        self.assertTrue(prime_num(103))
        self.assertTrue(prime_num(107))
