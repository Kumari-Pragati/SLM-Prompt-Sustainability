import unittest
from mbpp_605_code import prime_num

class TestPrimeNum(unittest.TestCase):

    def test_simple_prime(self):
        self.assertTrue(prime_num(2))
        self.assertTrue(prime_num(3))
        self.assertTrue(prime_num(5))
        self.assertTrue(prime_num(7))

    def test_simple_non_prime(self):
        self.assertFalse(prime_num(1))
        self.assertFalse(prime_num(4))
        self.assertFalse(prime_num(6))
        self.assertFalse(prime_num(8))

    def test_edge_conditions(self):
        self.assertFalse(prime_num(0))
        self.assertFalse(prime_num(-1))
        self.assertFalse(prime_num(-5))

    def test_large_prime(self):
        self.assertTrue(prime_num(131))
        self.assertTrue(prime_num(997))

    def test_large_non_prime(self):
        self.assertFalse(prime_num(100))
        self.assertFalse(prime_num(400))

    def test_max_value(self):
        self.assertTrue(prime_num(2147483647))

    def test_min_value(self):
        self.assertFalse(prime_num(-2147483648))
