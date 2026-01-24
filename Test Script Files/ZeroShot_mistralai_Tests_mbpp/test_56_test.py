import unittest
from mbpp_56_code import check, rev

class TestCheckFunction(unittest.TestCase):

    def test_check_positive_numbers(self):
        self.assertTrue(check(21))
        self.assertTrue(check(55))
        self.assertTrue(check(101))

    def test_check_zero(self):
        self.assertFalse(check(0))

    def test_check_negative_numbers(self):
        self.assertFalse(check(-1))
        self.assertFalse(check(-21))
        self.assertFalse(check(-55))

    def test_edge_cases(self):
        self.assertFalse(check(1))
        self.assertFalse(check(2))
        self.assertTrue(check(3))
        self.assertFalse(check(4))
        self.assertFalse(check(9))
        self.assertTrue(check(10))
        self.assertFalse(check(11))
        self.assertFalse(check(12))
        self.assertTrue(check(13))
        self.assertFalse(check(14))
        self.assertFalse(check(15))
        self.assertFalse(check(16))
        self.assertFalse(check(17))
        self.assertFalse(check(18))
        self.assertFalse(check(19))
        self.assertTrue(check(20))
