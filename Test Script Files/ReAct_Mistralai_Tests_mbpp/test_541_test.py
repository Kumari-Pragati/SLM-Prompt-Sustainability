import unittest
from mbpp_541_code import check_abundant

class TestCheckAbundant(unittest.TestCase):

    def test_perfect_numbers(self):
        self.assertTrue(check_abundant(6))
        self.assertTrue(check_abundant(28))
        self.assertTrue(check_abundant(496))

    def test_abundant_numbers(self):
        self.assertTrue(check_abundant(12))
        self.assertTrue(check_abundant(36))
        self.assertTrue(check_abundant(8710))

    def test_non_abundant_numbers(self):
        self.assertFalse(check_abundant(5))
        self.assertFalse(check_abundant(10))
        self.assertFalse(check_abundant(15))

    def test_zero_and_negative_numbers(self):
        self.assertFalse(check_abundant(0))
        self.assertFalse(check_abundant(-1))

    def test_one_and_prime_numbers(self):
        self.assertFalse(check_abundant(1))
        self.assertFalse(check_abundant(3))
        self.assertFalse(check_abundant(5))
