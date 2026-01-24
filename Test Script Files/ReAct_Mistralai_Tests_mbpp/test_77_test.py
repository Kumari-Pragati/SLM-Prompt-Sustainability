import unittest
from mbpp_77_code import is_Diff

class TestIsDiff(unittest.TestCase):

    def test_positive_numbers(self):
        """Test positive numbers divisible by 11"""
        self.assertTrue(is_Diff(11))
        self.assertTrue(is_Diff(22))
        self.assertTrue(is_Diff(99))
        self.assertTrue(is_Diff(1000))

    def test_zero(self):
        """Test if 0 is not divisible by 11"""
        self.assertFalse(is_Diff(0))

    def test_negative_numbers(self):
        """Test negative numbers divisible by 11"""
        self.assertTrue(is_Diff(-11))
        self.assertTrue(is_Diff(-22))
        self.assertTrue(is_Diff(-99))
        self.assertTrue(is_Diff(-1000))

    def test_large_number(self):
        """Test a very large number"""
        self.assertTrue(is_Diff(100000011))

    def test_non_multiple_of_11(self):
        """Test a number not divisible by 11"""
        self.assertFalse(is_Diff(10))
        self.assertFalse(is_Diff(12))
        self.assertFalse(is_Diff(13))
