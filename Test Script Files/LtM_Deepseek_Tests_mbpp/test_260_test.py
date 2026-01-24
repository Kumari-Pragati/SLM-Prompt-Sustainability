import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):

    def test_newman_prime_simple(self):
        self.assertEqual(newman_prime(0), 1)
        self.assertEqual(newman_prime(1), 1)

    def test_newman_prime_edge(self):
        self.assertEqual(newman_prime(2), 4)
        self.assertEqual(newman_prime(3), 10)

    def test_newman_prime_complex(self):
        self.assertEqual(newman_prime(4), 26)
        self.assertEqual(newman_prime(5), 70)
