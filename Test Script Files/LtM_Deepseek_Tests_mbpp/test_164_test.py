import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertTrue(areEquivalent(10, 18))
        self.assertTrue(areEquivalent(6, 21))

    def test_edge_conditions(self):
        self.assertTrue(areEquivalent(0, 0))
        self.assertFalse(areEquivalent(1, 2))

    def test_boundary_conditions(self):
        self.assertTrue(areEquivalent(28, 28))
        self.assertFalse(areEquivalent(100, 200))

    def test_complex_cases(self):
        self.assertFalse(areEquivalent(1000, 2000))
        self.assertTrue(areEquivalent(164, 164))
