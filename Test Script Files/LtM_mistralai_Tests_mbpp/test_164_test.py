import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):

    def test_simple_equivalent(self):
        self.assertTrue(areEquivalent(12, 28))
        self.assertTrue(areEquivalent(16, 16))

    def test_simple_not_equivalent(self):
        self.assertFalse(areEquivalent(12, 29))
        self.assertFalse(areEquivalent(16, 17))

    def test_edge_cases(self):
        self.assertTrue(areEquivalent(1, 1))
        self.assertTrue(areEquivalent(2, 4))
        self.assertFalse(areEquivalent(0, 1))
        self.assertFalse(areEquivalent(1, 0))

    def test_large_numbers(self):
        self.assertTrue(areEquivalent(1000000, 1000001))
        self.assertFalse(areEquivalent(1000000, 1000002))
