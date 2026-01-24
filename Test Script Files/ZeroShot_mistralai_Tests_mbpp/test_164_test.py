import unittest
from mbpp_164_code import areEquivalent, divSum

class TestAreEquivalent(unittest.TestCase):

    def test_are_equivalent_same_numbers(self):
        self.assertTrue(areEquivalent(1, 1))
        self.assertTrue(areEquivalent(2, 2))
        self.assertTrue(areEquivalent(3, 3))

    def test_are_equivalent_different_numbers(self):
        self.assertFalse(areEquivalent(1, 2))
        self.assertFalse(areEquivalent(2, 3))
        self.assertFalse(areEquivalent(3, 4))

    def test_are_equivalent_large_numbers(self):
        self.assertTrue(areEquivalent(10, 1))  # 1 + 10 + 5 = 16, 1 + 10 = 11
        self.assertTrue(areEquivalent(100, 1))  # 1 + 100 + 99 = 199, 1 + 100 = 101
        self.assertTrue(areEquivalent(1000, 1))  # 1 + 1000 + 999 = 2000, 1 + 1000 = 1001

    def test_are_equivalent_negative_numbers(self):
        self.assertTrue(areEquivalent(-1, -1))
        self.assertTrue(areEquivalent(-2, -2))
        self.assertTrue(areEquivalent(-3, -3))

    def test_are_equivalent_zero(self):
        self.assertFalse(areEquivalent(0, 1))
        self.assertFalse(areEquivalent(1, 0))
        self.assertFalse(areEquivalent(0, 0))
