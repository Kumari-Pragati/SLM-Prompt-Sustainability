import unittest
from mbpp_762_code import check_monthnumber_number

class TestCheckMonthnumberNumber(unittest.TestCase):
    def test_valid_month_numbers(self):
        self.assertTrue(check_monthnumber_number(4))
        self.assertTrue(check_monthnumber_number(6))
        self.assertTrue(check_monthnumber_number(9))
        self.assertTrue(check_month_number(11))

    def test_invalid_month_numbers(self):
        self.assertFalse(check_monthnumber_number(1))
        self.assertFalse(check_monthnumber_number(2))
        self.assertFalse(check_monthnumber_number(3))
        self.assertFalse(check_monthnumber_number(5))
        self.assertFalse(check_monthnumber_number(7))
        self.assertFalse(check_monthnumber_number(8))
        self.assertFalse(check_monthnumber_number(10))
        self.assertFalse(check_monthnumber_number(12))

    def test_edge_cases(self):
        self.assertFalse(check_monthnumber_number(0))
        self.assertFalse(check_monthnumber_number(13))
