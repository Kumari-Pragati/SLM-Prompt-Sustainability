import unittest
from mbpp_260_code import newman_prime

class TestNewmanPrime(unittest.TestCase):

    def test_newman_prime_zero(self):
        self.assertEqual(newman_prime(0), 1)

    def test_newman_prime_one(self):
        self.assertEqual(newman_prime(1), 1)

    def test_newman_prime_two(self):
        self.assertEqual(newman_prime(2), 2)

    def test_newman_prime_three(self):
        self.assertEqual(newman_prime(3), 3)

    def test_newman_prime_four(self):
        self.assertEqual(newman_prime(4), 5)

    def test_newman_prime_five(self):
        self.assertEqual(newman_prime(5), 13)

    def test_newman_prime_six(self):
        self.assertEqual(newman_prime(6), 29)

    def test_newman_prime_seven(self):
        self.assertEqual(newman_prime(7), 57)

    def test_newman_prime_eight(self):
        self.assertEqual(newman_prime(8), 97)

    def test_newman_prime_nine(self):
        self.assertEqual(newman_prime(9), 161)

    def test_newman_prime_ten(self):
        self.assertEqual(newman_prime(10), 265)
