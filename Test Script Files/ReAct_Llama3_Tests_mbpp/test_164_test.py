import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):

    def test_equivalent_numbers(self):
        self.assertTrue(areEquivalent(12, 18))

    def test_non_equivalent_numbers(self):
        self.assertFalse(areEquivalent(12, 15))

    def test_single_digit_numbers(self):
        self.assertTrue(areEquivalent(1, 1))

    def test_divisible_numbers(self):
        self.assertTrue(areEquivalent(12, 24))

    def test_prime_numbers(self):
        self.assertFalse(areEquivalent(11, 13))

    def test_zero(self):
        self.assertTrue(areEquivalent(0, 0))

    def test_negative_numbers(self):
        self.assertTrue(areEquivalent(-12, -18))

    def test_large_numbers(self):
        self.assertTrue(areEquivalent(1000, 2000))
