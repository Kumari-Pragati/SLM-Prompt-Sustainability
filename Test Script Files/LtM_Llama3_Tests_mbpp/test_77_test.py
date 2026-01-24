import unittest
from mbpp_77_code import is_Diff

class TestIsDiff(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(is_Diff(0))
        self.assertTrue(is_Diff(11))
        self.assertTrue(is_Diff(22))
        self.assertTrue(is_Diff(33))

    def test_simple_invalid(self):
        self.assertFalse(is_Diff(1))
        self.assertFalse(is_Diff(2))
        self.assertFalse(is_Diff(3))
        self.assertFalse(is_Diff(4))

    def test_edge_cases(self):
        self.assertTrue(is_Diff(-11))
        self.assertTrue(is_Diff(-22))
        self.assertFalse(is_Diff(-1))
        self.assertFalse(is_Diff(-2))

    def test_boundary_cases(self):
        self.assertTrue(is_Diff(10))
        self.assertFalse(is_Diff(1))
