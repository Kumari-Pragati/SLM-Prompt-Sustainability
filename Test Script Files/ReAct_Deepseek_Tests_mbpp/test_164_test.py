import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(areEquivalent(10, 15))
        self.assertTrue(areEquivalent(12, 28))
        self.assertFalse(areEquivalent(10, 20))

    def test_edge_cases(self):
        self.assertTrue(areEquivalent(1, 1))
        self.assertFalse(areEquivalent(10, 21))
        self.assertTrue(areEquivalent(0, 0))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            areEquivalent("10", 15)
        with self.assertRaises(TypeError):
            areEquivalent(10, "15")
        with self.assertRaises(TypeError):
            areEquivalent("10", "15")
