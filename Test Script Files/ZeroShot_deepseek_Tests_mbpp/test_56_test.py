import unittest
from mbpp_56_code import check

class TestCheckFunction(unittest.TestCase):

    def test_check_positive_numbers(self):
        self.assertTrue(check(11))
        self.assertTrue(check(121))
        self.assertTrue(check(3443))
        self.assertTrue(check(12321))

    def test_check_negative_numbers(self):
        self.assertFalse(check(-11))
        self.assertFalse(check(-121))
        self.assertFalse(check(-3443))
        self.assertFalse(check(-12321))

    def test_check_zero(self):
        self.assertFalse(check(0))

    def test_check_large_numbers(self):
        self.assertTrue(check(1234321))
        self.assertFalse(check(12344321))
