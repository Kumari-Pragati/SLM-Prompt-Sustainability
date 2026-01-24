import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(newman_prime(0), 1)

    def test_one(self):
        self.assertEqual(newman_prime(1), 1)

    def test_small_positive(self):
        self.assertEqual(newman_prime(2), 3)

    def test_small_positive_edge(self):
        self.assertEqual(newman_prime(3), 11)

    def test_large_positive(self):
        self.assertEqual(newman_prime(10), 177)

    def test_negative(self):
        with self.assertRaises(ValueError):
            newman_prime(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            newman_prime(2.5)
