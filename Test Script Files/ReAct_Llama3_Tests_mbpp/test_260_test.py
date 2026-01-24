import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(newman_prime(0), 1)

    def test_one(self):
        self.assertEqual(newman_prime(1), 1)

    def test_small_prime(self):
        self.assertEqual(newman_prime(2), 2)

    def test_small_composite(self):
        self.assertEqual(newman_prime(3), 5)

    def test_larger_prime(self):
        self.assertEqual(newman_prime(5), 41)

    def test_larger_composite(self):
        self.assertEqual(newman_prime(6), 97)

    def test_negative(self):
        with self.assertRaises(ValueError):
            newman_prime(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            newman_prime(2.5)
