import unittest
from mbpp_541_code import check_abundant

class TestAbundant(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(check_abundant(12))
        self.assertTrue(check_abundant(18))
        self.assertFalse(check_abundant(10))
        self.assertFalse(check_abundant(20))

    def test_negative_numbers(self):
        self.assertFalse(check_abundant(-10))
        self.assertFalse(check_abundant(-20))

    def test_zero(self):
        self.assertFalse(check_abundant(0))

    def test_large_numbers(self):
        self.assertTrue(check_abundant(28))
        self.assertFalse(check_abundant(27))
