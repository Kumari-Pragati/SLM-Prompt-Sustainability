import unittest
from mbpp_56_code import check

class TestCheckFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(check(15))
        self.assertTrue(check(32))
        self.assertTrue(check(2017))

    def test_zero(self):
        self.assertFalse(check(0))

    def test_negative_numbers(self):
        self.assertFalse(check(-1))
        self.assertFalse(check(-32))
        self.assertFalse(check(-2017))

    def test_large_numbers(self):
        self.assertTrue(check(999999999))
        self.assertTrue(check(10000000001))

    def test_single_digit_numbers(self):
        self.assertTrue(check(2))
        self.assertTrue(check(5))
        self.assertFalse(check(0))
        self.assertFalse(check(1))
        self.assertFalse(check(3))
        self.assertFalse(check(4))
        self.assertFalse(check(6))
        self.assertFalse(check(7))
        self.assertFalse(check(8))
        self.assertFalse(check(9))
