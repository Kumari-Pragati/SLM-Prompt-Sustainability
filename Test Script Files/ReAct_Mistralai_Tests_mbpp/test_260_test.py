import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(newman_prime(0), 1)

    def test_one(self):
        self.assertEqual(newman_prime(1), 1)

    def test_positive_small(self):
        self.assertEqual(newman_prime(2), 3)
        self.assertEqual(newman_prime(3), 7)
        self.assertEqual(newman_prime(4), 15)

    def test_positive_large(self):
        self.assertEqual(newman_prime(100), 32768203816775807)

    def test_negative(self):
        with self.assertRaises(ValueError):
            newman_prime(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            newman_prime(3.14)
