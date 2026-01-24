import unittest
from mbpp_77_code import is_Diff

class TestIsDiff(unittest.TestCase):
    def test_divisible_by_11(self):
        self.assertTrue(is_Diff(11))
        self.assertTrue(is_Diff(22))
        self.assertTrue(is_Diff(33))

    def test_not_divisible_by_11(self):
        self.assertFalse(is_Diff(10))
        self.assertFalse(is_Diff(12))
        self.assertFalse(is_Diff(13))

    def test_zero(self):
        self.assertFalse(is_Diff(0))

    def test_negative_numbers(self):
        self.assertFalse(is_Diff(-1))
        self.assertFalse(is_Diff(-11))
        self.assertFalse(is_Diff(-22))
