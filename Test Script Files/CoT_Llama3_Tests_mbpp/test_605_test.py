import unittest
from mbpp_605_code import prime_num

class TestPrimeNum(unittest.TestCase):
    def test_prime_num_positive(self):
        self.assertTrue(prime_num(5))
        self.assertTrue(prime_num(7))
        self.assertTrue(prime_num(11))

    def test_prime_num_negative(self):
        self.assertFalse(prime_num(-1))
        self.assertFalse(prime_num(-5))
        self.assertFalse(prime_num(-10))

    def test_prime_num_zero(self):
        self.assertFalse(prime_num(0))

    def test_prime_num_one(self):
        self.assertTrue(prime_num(1))

    def test_prime_num_edge(self):
        self.assertTrue(prime_num(2))
        self.assertTrue(prime_num(3))
        self.assertFalse(prime_num(4))

    def test_prime_num_large(self):
        self.assertTrue(prime_num(1000))
        self.assertTrue(prime_num(1001))
        self.assertFalse(prime_num(1002))

    def test_prime_num_invalid(self):
        with self.assertRaises(TypeError):
            prime_num('a')
        with self.assertRaises(TypeError):
            prime_num(None)
