import unittest
from77_code import is_Diff

class TestIsDiff(unittest.TestCase):
    def test_positive(self):
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

    def test_zero(self):
        self.assertFalse(is_Diff(0))

    def test_negative(self):
        self.assertTrue(is_Diff(-11))
        self.assertTrue(is_Diff(-22))
        self.assertTrue(is_Diff(-33))
        self.assertTrue(is_Diff(-44))
        self.assertTrue(is_Diff(-55))
        self.assertTrue(is_Diff(-66))
        self.assertTrue(is_Diff(-77))
        self.assertTrue(is_Diff(-88))
        self.assertTrue(is_Diff(-99))
        self.assertTrue(is_Diff(-110))

    def test_floats(self):
        self.assertFalse(is_Diff(11.0))
        self.assertFalse(is_Diff(22.0))
        self.assertFalse(is_Diff(33.0))
        self.assertFalse(is_Diff(44.0))
        self.assertFalse(is_Diff(55.0))
        self.assertFalse(is_Diff(66.0))
        self.assertFalse(is_Diff(77.0))
        self.assertFalse(is_Diff(88.0))
        self.assertFalse(is_Diff(99.0))
        self.assertFalse(is_Diff(110.0))
