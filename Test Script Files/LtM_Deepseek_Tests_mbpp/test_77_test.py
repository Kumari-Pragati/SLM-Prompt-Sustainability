import unittest
from mbpp_77_code import is_Diff

class TestIsDiff(unittest.TestCase):

    def test_simple_cases(self):
        self.assertTrue(is_Diff(11))
        self.assertTrue(is_Diff(22))
        self.assertFalse(is_Diff(10))
        self.assertFalse(is_Diff(20))

    def test_edge_conditions(self):
        self.assertFalse(is_Diff(0))
        self.assertFalse(is_Diff(-11))
        self.assertFalse(is_Diff(77))

    def test_complex_cases(self):
        self.assertFalse(is_Diff(111))
        self.assertFalse(is_Diff(-111))
        self.assertFalse(is_Diff(777))
        self.assertTrue(is_Diff(121))
        self.assertTrue(is_Diff(-121))
        self.assertFalse(is_Diff(767))
