import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(newman_prime(0), 1)

    def test_one(self):
        self.assertEqual(newman_prime(1), 1)

    def test_small_numbers(self):
        self.assertEqual(newman_prime(2), 3)
        self.assertEqual(newman_prime(3), 7)
        self.assertEqual(newman_prime(4), 13)
        self.assertEqual(newman_prime(5), 29)
        self.assertEqual(newman_prime(6), 47)

    def test_large_numbers(self):
        self.assertEqual(newman_prime(100), 123765393532946740)
        self.assertEqual(newman_prime(1000), 16777216029300500868288)
