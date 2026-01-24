import unittest
from mbpp_541_code import check_abundant

class TestCheckAbundant(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(check_abundant(12))
        self.assertTrue(check_abundant(24))
        self.assertFalse(check_abundant(7))

    def test_edge_cases(self):
        self.assertFalse(check_abundant(1))
        self.assertFalse(check_abundant(2))
        self.assertFalse(check_abundant(3))

    def test_boundary_cases(self):
        self.assertFalse(check_abundant(4))
        self.assertFalse(check_abundant(5))
        self.assertFalse(check_abundant(6))

    def test_corner_cases(self):
        self.assertFalse(check_abundant(8))
        self.assertFalse(check_abundant(9))
        self.assertFalse(check_abundant(10))
