import unittest
from mbpp_541_code import check_abundant

class TestCheckAbundant(unittest.TestCase):
    def test_abundant_number(self):
        self.assertTrue(check_abundant(12))

    def test_perfect_number(self):
        self.assertTrue(check_abundant(28))

    def test_near_perfect_number(self):
        self.assertTrue(check_abundant(27))

    def test_non_abundant_number(self):
        self.assertFalse(check_abundant(11))

    def test_zero(self):
        self.assertFalse(check_abundant(0))

    def test_negative_number(self):
        self.assertFalse(check_abundant(-1))
