import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(newman_prime(0), 1)

    def test_one(self):
        self.assertEqual(newman_prime(1), 1)

    def test_small_positive_numbers(self):
        self.assertEqual(newman_prime(2), 3)
        self.assertEqual(newman_prime(3), 11)
        self.assertEqual(newman_prime(4), 23)
        self.assertEqual(newman_prime(5), 53)

    def test_large_positive_numbers(self):
        self.assertEqual(newman_prime(10), 251)
        self.assertEqual(newman_prime(20), 302)
        self.assertEqual(newman_prime(30), 541)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            newman_prime(-1)

    def test_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            newman_prime(2.5)
