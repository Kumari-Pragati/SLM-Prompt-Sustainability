import unittest
from mbpp_56_code import check

class TestCheck(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(check(123))
        self.assertTrue(check(987))

    def test_zero(self):
        self.assertFalse(check(0))

    def test_negative_numbers(self):
        self.assertFalse(check(-123))
        self.assertFalse(check(-987))

    def test_large_numbers(self):
        self.assertTrue(check(123456789))
        self.assertTrue(check(987654321))

    def test_single_digit_numbers(self):
        self.assertTrue(check(1))
        self.assertTrue(check(2))
        self.assertTrue(check(3))
        self.assertTrue(check(4))
        self.assertTrue(check(5))
        self.assertTrue(check(6))
        self.assertTrue(check(7))
        self.assertTrue(check(8))
        self.assertTrue(check(9))
