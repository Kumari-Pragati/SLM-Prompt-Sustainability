import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertTrue(areEquivalent(12, 15))
        self.assertTrue(areEquivalent(6, 10))

    def test_edge_cases(self):
        self.assertFalse(areEquivalent(0, 0))
        self.assertFalse(areEquivalent(1, 2))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            areEquivalent("12", 15)
        with self.assertRaises(TypeError):
            areEquivalent(12, "15")
        with self.assertRaises(TypeError):
            areEquivalent("12", "15")
