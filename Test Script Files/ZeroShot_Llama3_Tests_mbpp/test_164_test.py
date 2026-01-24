import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):

    def test_areEquivalent_true(self):
        self.assertTrue(areEquivalent(12, 18))

    def test_areEquivalent_false(self):
        self.assertFalse(areEquivalent(12, 20))

    def test_areEquivalent_same_number(self):
        self.assertTrue(areEquivalent(12, 12))

    def test_areEquivalent_non_integer(self):
        with self.assertRaises(TypeError):
            areEquivalent(12.5, 18)

    def test_areEquivalent_negative_numbers(self):
        self.assertFalse(areEquivalent(-12, -18))

    def test_areEquivalent_zero(self):
        self.assertTrue(areEquivalent(0, 0))
