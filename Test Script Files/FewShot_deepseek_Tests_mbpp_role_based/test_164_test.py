import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(areEquivalent(10, 18))

    def test_edge_case(self):
        self.assertFalse(areEquivalent(1, 2))

    def test_boundary_conditions(self):
        self.assertTrue(areEquivalent(0, 0))
        self.assertFalse(areEquivalent(1, 0))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            areEquivalent("10", 18)
        with self.assertRaises(TypeError):
            areEquivalent(10, "18")
        with self.assertRaises(TypeError):
            areEquivalent("10", "18")
