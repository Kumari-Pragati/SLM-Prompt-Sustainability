import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):

    def test_same_perfect_numbers(self):
        self.assertTrue(areEquivalent(6, 28))

    def test_different_perfect_numbers(self):
        self.assertFalse(areEquivalent(6, 24))

    def test_one_number_is_perfect(self):
        self.assertTrue(areEquivalent(6, 20))
        self.assertTrue(areEquivalent(28, 6))

    def test_one_number_is_not_perfect(self):
        self.assertFalse(areEquivalent(6, 7))
        self.assertFalse(areEquivalent(28, 29))

    def test_zero(self):
        self.assertRaises(ValueError, areEquivalent, 0)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, areEquivalent, -1)
        self.assertRaises(ValueError, areEquivalent, -28)
