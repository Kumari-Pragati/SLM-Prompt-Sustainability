import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(areEquivalent(10, 18))
        self.assertTrue(areEquivalent(12, 28))

    def test_edge_cases(self):
        self.assertTrue(areEquivalent(1, 1))
        self.assertFalse(areEquivalent(10, 20))

    def test_boundary_cases(self):
        self.assertTrue(areEquivalent(0, 0))
        self.assertFalse(areEquivalent(1, 0))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            areEquivalent("10", 18)
        with self.assertRaises(TypeError):
            areEquivalent(10, "18")
        with self.assertRaises(TypeError):
            areEquivalent("10", "18")
