import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):
    def test_small_positive_numbers(self):
        self.assertEqual(newman_prime(0), 1)
        self.assertEqual(newman_prime(1), 1)
        self.assertEqual(newman_prime(2), 3)
        self.assertEqual(newman_prime(3), 7)
        self.assertEqual(newman_prime(4), 15)

    def test_large_positive_numbers(self):
        self.assertEqual(newman_prime(100), 327675)
        self.assertEqual(newman_prime(1000), 2674447948918362847477)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, newman_prime, -1)
        self.assertRaises(ValueError, newman_prime, -2)
