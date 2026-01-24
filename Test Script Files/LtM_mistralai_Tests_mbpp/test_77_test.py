import unittest
from mbpp_77_code import is_Diff

class TestIsDiff(unittest.TestCase):
    def test_simple_positive(self):
        self.assertTrue(is_Diff(11))

    def test_simple_negative(self):
        self.assertFalse(is_Diff(10))

    def test_edge_cases(self):
        self.assertTrue(is_Diff(0))
        self.assertTrue(is_Diff(22))

    def test_complex_cases(self):
        self.assertTrue(is_Diff(-11))
        self.assertTrue(is_Diff(1100))
