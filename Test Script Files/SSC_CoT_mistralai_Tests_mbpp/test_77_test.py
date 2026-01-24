import unittest
from mbpp_77_code import sentinel

from77_code import is_Diff

class TestIsDiff(unittest.TestCase):
    def test_normal_input(self):
        self.assertTrue(is_Diff(11 * 2))
        self.assertTrue(is_Diff(11 * 3))

    def test_edge_cases(self):
        self.assertTrue(is_Diff(0))
        self.assertTrue(is_Diff(11 - 1))
        self.assertTrue(is_Diff(11 + 1))

    def test_boundary_cases(self):
        self.assertFalse(is_Diff(10))
        self.assertTrue(is_Diff(12))

    def test_invalid_input(self):
        self.assertRaises(TypeError, is_Diff, sentinel.invalid_input)
