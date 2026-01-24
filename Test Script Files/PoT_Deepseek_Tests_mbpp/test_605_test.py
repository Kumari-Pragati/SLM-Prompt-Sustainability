import unittest
from mbpp_605_code import prime_num

class TestPrimeNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(prime_num(2))
        self.assertTrue(prime_num(3))
        self.assertFalse(prime_num(4))
        self.assertTrue(prime_num(5))
        self.assertFalse(prime_num(6))
        self.assertFalse(prime_num(7))
        self.assertFalse(prime_num(8))
        self.assertFalse(prime_num(9))
        self.assertFalse(prime_num(10))

    def test_edge_cases(self):
        self.assertFalse(prime_num(0))
        self.assertFalse(prime_num(1))

    def test_boundary_cases(self):
        self.assertTrue(prime_num(2))
        self.assertFalse(prime_num(3))
        self.assertFalse(prime_num(4))
        self.assertFalse(prime_num(5))
        self.assertFalse(prime_num(6))
        self.assertFalse(prime_num(7))
        self.assertFalse(prime_num(8))
        self.assertFalse(prime_num(9))
        self.assertFalse(prime_num(10))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            prime_num('a')
        with self.assertRaises(TypeError):
            prime_num(None)
        with self.assertRaises(TypeError):
            prime_num([])
