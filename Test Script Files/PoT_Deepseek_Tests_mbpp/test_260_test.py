import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(newman_prime(0), 1)
        self.assertEqual(newman_prime(1), 1)
        self.assertEqual(newman_prime(2), 4)
        self.assertEqual(newman_prime(3), 10)
        self.assertEqual(newman_prime(4), 28)

    def test_edge_cases(self):
        self.assertEqual(newman_prime(-1), 1)
        self.assertEqual(newman_prime(-10), 1)

    def test_corner_cases(self):
        self.assertEqual(newman_prime(100), 2048)
        self.assertEqual(newman_prime(200), 16384)
