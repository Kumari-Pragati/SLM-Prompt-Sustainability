import unittest
from mbpp_605_code import prime_num

class TestPrimeNum(unittest.TestCase):
    def test_prime_num_typical(self):
        self.assertTrue(prime_num(2))
        self.assertTrue(prime_num(3))
        self.assertTrue(prime_num(5))
        self.assertTrue(prime_num(7))
        self.assertTrue(prime_num(11))
        self.assertTrue(prime_num(13))
        self.assertTrue(prime_num(17))
        self.assertTrue(prime_num(19))
        self.assertTrue(prime_num(23))
        self.assertTrue(prime_num(29))

    def test_prime_num_edge_and_boundary(self):
        self.assertTrue(prime_num(0))  # Edge case: zero is not a prime number
        self.assertFalse(prime_num(1))  # Edge case: one is not a prime number
        self.assertTrue(prime_num(4))  # Boundary case: 4 is not prime but within the function's range
        self.assertFalse(prime_num(6))  # Boundary case: 6 is not prime but within the function's range
        self.assertFalse(prime_num(20))  # Boundary case: 20 is not prime but within the function's range
        self.assertTrue(prime_num(31))  # Edge case: 31 is a prime number but the function's range goes up to 30
        self.assertTrue(prime_num(101))  # Edge case: 101 is a prime number but the function's range goes up to 50
