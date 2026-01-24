import unittest
from mbpp_77_code import is_Diff

class TestIsDiff(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_Diff(0))
        self.assertTrue(is_Diff(11))
        self.assertTrue(is_Diff(22))
        self.assertTrue(is_Diff(33))
        self.assertTrue(is_Diff(44))
        self.assertTrue(is_Diff(55))
        self.assertTrue(is_Diff(66))
        self.assertTrue(is_Diff(77))
        self.assertTrue(is_Diff(88))
        self.assertTrue(is_Diff(99))
        self.assertTrue(is_Diff(110))

    def test_edge_and_boundary_cases(self):
        self.assertFalse(is_Diff(-1))
        self.assertFalse(is_Diff(0.1))
        self.assertFalse(is_Diff(1))
        self.assertFalse(is_Diff(10))
        self.assertFalse(is_Diff(111))
        self.assertFalse(is_Diff(200))
