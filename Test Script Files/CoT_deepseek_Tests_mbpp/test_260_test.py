import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):

    def test_newman_prime_typical_cases(self):
        self.assertEqual(newman_prime(0), 1)
        self.assertEqual(newman_prime(1), 1)
        self.assertEqual(newman_prime(2), 4)
        self.assertEqual(newman_prime(3), 10)
        self.assertEqual(newman_prime(4), 28)

    def test_newman_prime_edge_cases(self):
        self.assertEqual(newman_prime(-1), 1)
        self.assertEqual(newman_prime(-10), 1)
        self.assertEqual(newman_prime(5), 120)
        self.assertEqual(newman_prime(10), 167188952980)

    def test_newman_prime_invalid_inputs(self):
        with self.assertRaises(RecursionError):
            newman_prime(20)
