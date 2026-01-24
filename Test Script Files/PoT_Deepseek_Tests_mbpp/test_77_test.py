import unittest
from mbpp_77_code import is_Diff

class TestIsDiff(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_Diff(11))
        self.assertTrue(is_Diff(22))
        self.assertTrue(is_Diff(33))
        self.assertFalse(is_Diff(10))
        self.assertFalse(is_Diff(20))
        self.assertFalse(is_Diff(30))

    def test_edge_cases(self):
        self.assertFalse(is_Diff(0))
        self.assertFalse(is_Diff(-11))
        self.assertFalse(is_Diff(-22))
        self.assertFalse(is_Diff(-33))

    def test_corner_cases(self):
        self.assertFalse(is_Diff(1))
        self.assertFalse(is_Diff(2))
        self.assertFalse(is_Diff(3))
        self.assertFalse(is_Diff(4))
        self.assertFalse(is_Diff(5))
        self.assertFalse(is_Diff(6))
        self.assertFalse(is_Diff(7))
        self.assertFalse(is_Diff(8))
        self.assertFalse(is_Diff(9))
        self.assertFalse(is_Diff(10))
