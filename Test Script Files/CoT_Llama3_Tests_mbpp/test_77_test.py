import unittest
from mbpp_77_code import is_Diff

class TestIsDiff(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_Diff(11))

    def test_false(self):
        self.assertFalse(is_Diff(10))

    def test_zero(self):
        self.assertFalse(is_Diff(0))

    def test_negative(self):
        self.assertFalse(is_Diff(-11))

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            is_Diff('a')

    def test_edge_case(self):
        self.assertTrue(is_Diff(22))
