import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(newman_prime(0), 1)

    def test_one(self):
        self.assertEqual(newman_prime(1), 1)

    def test_positive_numbers(self):
        for n in range(2, 10):
            self.assertEqual(newman_prime(n), newman_prime(n - 1) + newman_prime(n - 2))

    def test_negative_numbers(self):
        for n in range(-1, -10, -1):
            self.assertEqual(newman_prime(n), newman_prime(-(n + 1)))

    def test_large_numbers(self):
        self.assertEqual(newman_prime(100), newman_prime(99) + newman_prime(98))

    def test_invalid_input_non_integer(self):
        self.assertRaises(TypeError, newman_prime, 'a')

    def test_invalid_input_negative_integer(self):
        self.assertRaises(ValueError, newman_prime, -1)
