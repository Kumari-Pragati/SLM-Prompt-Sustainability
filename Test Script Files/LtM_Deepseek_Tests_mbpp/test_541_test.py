import unittest
from mbpp_541_code import check_abundant

class TestCheckAbundant(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(check_abundant(12))
        self.assertFalse(check_abundant(8))

    def test_edge_conditions(self):
        self.assertFalse(check_abundant(0))
        self.assertFalse(check_abundant(-1))

    def test_boundary_conditions(self):
        self.assertFalse(check_abundant(1))
        self.assertTrue(check_abundant(12))
        self.assertFalse(check_abundant(28))

    def test_complex_cases(self):
        self.assertTrue(check_abundant(945))
        self.assertFalse(check_abundant(1000))
