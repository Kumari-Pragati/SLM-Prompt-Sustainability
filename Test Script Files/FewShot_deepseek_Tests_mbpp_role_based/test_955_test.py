import unittest
from mbpp_955_code import is_abundant

class TestIsAbundant(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(is_abundant(12))

    def test_edge_case(self):
        self.assertFalse(is_abundant(1))

    def test_boundary_case(self):
        self.assertFalse(is_abundant(0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_abundant('12')
