import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):
    def test_zero_input(self):
        self.assertEqual(newman_prime(0), 1)

    def test_one_input(self):
        self.assertEqual(newman_prime(1), 1)

    def test_small_positive_input(self):
        self.assertEqual(newman_prime(2), 2)

    def test_positive_input(self):
        self.assertEqual(newman_prime(3), 5)

    def test_larger_positive_input(self):
        self.assertEqual(newman_prime(4), 10)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            newman_prime(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            newman_prime(2.5)
