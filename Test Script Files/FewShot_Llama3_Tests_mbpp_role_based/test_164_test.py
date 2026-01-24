import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):
    def test_equivalent_numbers(self):
        self.assertTrue(areEquivalent(12, 18))

    def test_non_equivalent_numbers(self):
        self.assertFalse(areEquivalent(12, 15))

    def test_divisible_numbers(self):
        self.assertTrue(areEquivalent(36, 48))

    def test_non_divisible_numbers(self):
        self.assertFalse(areEquivalent(12, 25))

    def test_zero(self):
        self.assertTrue(areEquivalent(0, 0))

    def test_negative_numbers(self):
        self.assertTrue(areEquivalent(-12, -18))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            areEquivalent("12", 18)
