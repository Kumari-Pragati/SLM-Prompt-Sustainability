import unittest
from mbpp_541_code import check_abundant

class TestAbundantFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_abundant(12))

    def test_edge_case(self):
        self.assertFalse(check_abundant(1))

    def test_boundary_case(self):
        self.assertFalse(check_abundant(0))
        self.assertFalse(check_abundant(10000))

    def test_special_case(self):
        self.assertTrue(check_abundant(945))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_abundant('12')
        with self.assertRaises(ValueError):
            check_abundant(-12)
