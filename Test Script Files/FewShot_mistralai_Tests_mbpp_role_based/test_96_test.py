import unittest
from mbpp_96_code import divisor

class TestDivisor(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(divisor(12), 6)

    def test_zero(self):
        self.assertEqual(divisor(0), 1)

    def test_negative_number(self):
        self.assertEqual(divisor(-12), 1)

    def test_one(self):
        self.assertEqual(divisor(1), 1)

    def test_large_number(self):
        self.assertEqual(divisor(1000000), 1000000)

    def test_small_number(self):
        self.assertEqual(divisor(2), 1)

    def test_prime_number(self):
        self.assertEqual(divisor(5), 2)
