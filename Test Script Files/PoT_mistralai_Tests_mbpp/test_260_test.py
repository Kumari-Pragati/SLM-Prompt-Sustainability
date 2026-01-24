import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(newman_prime(0), 1)
        self.assertEqual(newman_prime(1), 1)
        self.assertEqual(newman_prime(2), 3)
        self.assertEqual(newman_prime(3), 7)
        self.assertEqual(newman_prime(4), 15)
        self.assertEqual(newman_prime(5), 31)
        self.assertEqual(newman_prime(6), 63)
        self.assertEqual(newman_prime(7), 127)
        self.assertEqual(newman_prime(8), 255)
        self.assertEqual(newman_prime(9), 511)

    def test_edge_cases(self):
        self.assertEqual(newman_prime(-1), None)
        self.assertEqual(newman_prime(10), None)
        self.assertEqual(newman_prime(20), None)
        self.assertEqual(newman_prime(30), None)
        self.assertEqual(newman_prime(40), None)
        self.assertEqual(newman_prime(50), None)
