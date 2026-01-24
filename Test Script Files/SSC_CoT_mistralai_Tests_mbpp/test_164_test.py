import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertTrue(areEquivalent(12, 28))
        self.assertTrue(areEquivalent(20, 20))
        self.assertTrue(areEquivalent(1, 1))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(areEquivalent(0, 1))
        self.assertFalse(areEquivalent(1, 0))
        self.assertTrue(areEquivalent(4, 16))
        self.assertTrue(areEquivalent(16, 4))
        self.assertFalse(areEquivalent(1, 2))
        self.assertFalse(areEquivalent(2, 3))
        self.assertFalse(areEquivalent(-1, 1))
        self.assertFalse(areEquivalent(1, -1))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, areEquivalent, 'a', 'b')
        self.assertRaises(TypeError, areEquivalent, 1.5, 2.5)
