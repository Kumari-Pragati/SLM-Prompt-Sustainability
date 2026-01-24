import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):

    def test_newman_prime_zero(self):
        self.assertEqual(newman_prime(0), 1)

    def test_newman_prime_one(self):
        self.assertEqual(newman_prime(1), 1)

    def test_newman_prime_two(self):
        self.assertEqual(newman_prime(2), 4)

    def test_newman_prime_three(self):
        self.assertEqual(newman_prime(3), 10)

    def test_newman_prime_four(self):
        self.assertEqual(newman_prime(4), 26)

    def test_newman_prime_negative(self):
        with self.assertRaises(RecursionError):
            newman_prime(-1)

    def test_newman_prime_large(self):
        with self.assertRaises(RecursionError):
            newman_prime(1000)
