import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):
    def test_equivalent_perfect_numbers(self):
        self.assertTrue(areEquivalent(6, 28))

    def test_equivalent_non_perfect_numbers(self):
        self.assertTrue(areEquivalent(24, 16))

    def test_equivalent_small_numbers(self):
        self.assertTrue(areEquivalent(4, 4))

    def test_equivalent_large_numbers(self):
        self.assertTrue(areEquivalent(1000, 2000))

    def test_non_equivalent_numbers(self):
        self.assertFalse(areEquivalent(4, 5))

    def test_zero(self):
        self.assertRaises(ValueError, areEquivalent, 0)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, areEquivalent, -1)
