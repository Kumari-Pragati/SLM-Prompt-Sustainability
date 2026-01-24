import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):

    def test_are_equivalent_positive(self):
        self.assertTrue(areEquivalent(12, 28))
        self.assertTrue(areEquivalent(20, 20))
        self.assertTrue(areEquivalent(1, 1))
        self.assertTrue(areEquivalent(2, 3))

    def test_are_equivalent_negative(self):
        self.assertFalse(areEquivalent(1, 2))
        self.assertFalse(areEquivalent(2, 4))
        self.assertFalse(areEquivalent(0, 1))
        self.assertFalse(areEquivalent(-1, 1))

    def test_edge_cases(self):
        self.assertTrue(areEquivalent(1, 1))
        self.assertTrue(areEquivalent(2, 3))
        self.assertTrue(areEquivalent(9, 81))
        self.assertTrue(areEquivalent(10, 121))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, areEquivalent, "string", 1)
        self.assertRaises(TypeError, areEquivalent, 1, "string")
        self.assertRaises(TypeError, areEquivalent, complex(1, 2), 3)
        self.assertRaises(TypeError, areEquivalent, 1, complex(1, 2))
