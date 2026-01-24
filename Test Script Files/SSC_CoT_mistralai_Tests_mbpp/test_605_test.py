import unittest
from mbpp_605_code import prime_num

class TestPrimeNum(unittest.TestCase):
    def test_prime_num_typical_inputs(self):
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
        self.assertTrue(prime_num(31))

    def test_prime_num_edge_cases(self):
        self.assertTrue(prime_num(0))  # edge case: zero is not a prime number
        self.assertFalse(prime_num(1))  # edge case: 1 is not a prime number
        self.assertTrue(prime_num(4))  # edge case: 2 is a factor of 4, so it's not prime
        self.assertFalse(prime_num(6))  # edge case: 2 and 3 are factors of 6, so it's not prime

    def test_prime_num_boundary_cases(self):
        self.assertTrue(prime_num(2**64 - 1))  # 2^64 - 1 is a Mersenne prime
        self.assertTrue(prime_num(2**31 - 1))  # 2^31 - 1 is a Fermat prime
        self.assertFalse(prime_num(2**32))  # 2^32 is not prime
