import unittest
from mbpp_605_code import prime_num

class TestPrimeNum(unittest.TestCase):

    def test_prime_num_typical_cases(self):
        self.assertTrue(prime_num(2))
        self.assertTrue(prime_num(3))
        self.assertTrue(prime_num(5))
        self.assertTrue(prime_num(7))
        self.assertFalse(prime_num(1))
        self.assertFalse(prime_num(4))
        self.assertFalse(prime_num(6))
        self.assertFalse(prime_num(8))

    def test_prime_num_edge_cases(self):
        self.assertFalse(prime_num(0))
        self.assertFalse(prime_num(-1))
        self.assertFalse(prime_num(-5))

    def test_prime_num_invalid_inputs(self):
        with self.assertRaises(TypeError):
            prime_num('5')
        with self.assertRaises(TypeError):
            prime_num(None)
        with self.assertRaises(TypeError):
            prime_num([1, 2, 3])
