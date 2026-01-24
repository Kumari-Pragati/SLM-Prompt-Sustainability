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

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            is_Diff('11')
        with self.assertRaises(TypeError):
            is_Diff(None)
