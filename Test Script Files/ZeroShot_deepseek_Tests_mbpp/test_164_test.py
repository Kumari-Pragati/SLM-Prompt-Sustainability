import unittest
from mbpp_164_code import areEquivalent

class TestAreEquivalent(unittest.TestCase):

    def test_areEquivalent(self):
        self.assertTrue(areEquivalent(12, 15))
        self.assertTrue(areEquivalent(6, 28))
        self.assertFalse(areEquivalent(10, 11))
        self.assertFalse(areEquivalent(12, 16))
        self.assertTrue(areEquivalent(1, 1))
