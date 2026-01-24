import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):
    def test_equivalent_numbers(self):
        self.assertTrue(areEquivalent(12, 18))
        self.assertTrue(areEquivalent(24, 36))
        self.assertTrue(areEquivalent(48, 60))

    def test_non_equivalent_numbers(self):
        self.assertFalse(areEquivalent(12, 15))
        self.assertFalse(areEquivalent(24, 30))
        self.assertFalse(areEquivalent(48, 50))

    def test_edge_cases(self):
        self.assertTrue(areEquivalent(1, 1))
        self.assertTrue(areEquivalent(2, 2))
        self.assertFalse(areEquivalent(1, 2))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            areEquivalent('a', 2)
        with self.assertRaises(TypeError):
            areEquivalent(1, 'b')
