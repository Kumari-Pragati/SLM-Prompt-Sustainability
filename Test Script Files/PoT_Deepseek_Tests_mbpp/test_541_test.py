import unittest
from mbpp_541_code import check_abundant

class TestCheckAbundant(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_abundant(12))
        self.assertFalse(check_abundant(8))

    def test_edge_cases(self):
        self.assertFalse(check_abundant(0))
        self.assertFalse(check_abundant(-1))

    def test_boundary_cases(self):
        self.assertFalse(check_abundant(1))
        self.assertTrue(check_abundant(12))

    def test_corner_cases(self):
        self.assertFalse(check_abundant(2))
        self.assertFalse(check_abundant(4))
        self.assertFalse(check_abundant(16))
