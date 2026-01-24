import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(newman_prime(0), 1)
        self.assertEqual(newman_prime(1), 1)
        self.assertEqual(newman_prime(2), 2)
        self.assertEqual(newman_prime(3), 6)
        self.assertEqual(newman_prime(4), 10)

    def test_edge(self):
        self.assertEqual(newman_prime(-1), 1)
        self.assertEqual(newman_prime(-2), 1)
        self.assertEqual(newman_prime(0), 1)
        self.assertEqual(newman_prime(1), 1)
        self.assertEqual(newman_prime(2), 2)

    def test_complex(self):
        self.assertEqual(newman_prime(5), 26)
        self.assertEqual(newman_prime(6), 52)
        self.assertEqual(newman_prime(7), 106)
