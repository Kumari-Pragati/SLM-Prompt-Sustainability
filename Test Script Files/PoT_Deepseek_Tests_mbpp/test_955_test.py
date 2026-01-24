import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_abundant(12))
        self.assertFalse(is_abundant(8))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(is_abundant(0))
        self.assertFalse(is_abundant(1))
        self.assertFalse(is_abundant(2))
        self.assertTrue(is_abundant(12))
        self.assertFalse(is_abundant(13))
        self.assertFalse(is_abundant(28))
        self.assertTrue(is_abundant(24))

    def test_corner_cases(self):
        self.assertFalse(is_abundant(945))
        self.assertTrue(is_abundant(947))
        self.assertFalse(is_abundant(949))
        self.assertTrue(is_abundant(951))
        self.assertFalse(is_abundant(953))
