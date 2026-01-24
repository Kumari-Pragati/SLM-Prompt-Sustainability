import unittest
from mbpp_605_code import prime_num

class TestPrimeNum(unittest.TestCase):
    def test_prime_num_typical(self):
        self.assertTrue(prime_num(5))
        self.assertTrue(prime_num(7))
        self.assertTrue(prime_num(11))

    def test_prime_num_edge(self):
        self.assertFalse(prime_num(1))
        self.assertFalse(prime_num(2))
        self.assertFalse(prime_num(4))

    def test_prime_num_boundary(self):
        self.assertTrue(prime_num(3))
        self.assertTrue(prime_num(6))
        self.assertTrue(prime_num(8))

    def test_prime_num_invalid(self):
        with self.assertRaises(TypeError):
            prime_num('a')
