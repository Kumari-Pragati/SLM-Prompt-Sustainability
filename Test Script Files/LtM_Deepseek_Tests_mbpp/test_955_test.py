import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertTrue(is_abundant(12))
        self.assertFalse(is_abundant(8))

    def test_edge_conditions(self):
        self.assertFalse(is_abundant(0))
        self.assertFalse(is_abundant(-1))

    def test_boundary_conditions(self):
        self.assertFalse(is_abundant(1))
        self.assertTrue(is_abundant(12))
        self.assertFalse(is_abundant(28))

    def test_complex_cases(self):
        self.assertTrue(is_abundant(945))
        self.assertFalse(is_abundant(1000))
