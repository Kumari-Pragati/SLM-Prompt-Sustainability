import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(areEquivalent(12, 28))
        self.assertTrue(areEquivalent(16, 22))
        self.assertTrue(areEquivalent(24, 12))

    def test_edge_case_small(self):
        self.assertFalse(areEquivalent(1, 2))
        self.assertFalse(areEquivalent(2, 1))

    def test_edge_case_large(self):
        self.assertTrue(areEquivalent(1000000000, 1000000000))

    def test_boundary_case_zero(self):
        self.assertFalse(areEquivalent(0, 0))

    def test_boundary_case_one(self):
        self.assertTrue(areEquivalent(1, 1))
