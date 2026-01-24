import unittest
from mbpp_762_code import check_monthnumber_number

class TestCheckMonthNumberNumber(unittest.TestCase):

    def test_valid_months(self):
        self.assertTrue(check_monthnumber_number(4))
        self.assertTrue(check_monthnumber_number(6))
        self.assertTrue(check_monthnumber_number(9))
        self.assertTrue(check_monthnumber_number(11))

    def test_invalid_months(self):
        self.assertFalse(check_monthnumber_number(1))
        self.assertFalse(check_monthnumber_number(2))
        self.assertFalse(check_monthnumber_number(3))
        self.assertFalse(check_monthnumber_number(12))
        self.assertFalse(check_monthnumber_number(-1))
        self.assertFalse(check_monthnumber_number(13))
