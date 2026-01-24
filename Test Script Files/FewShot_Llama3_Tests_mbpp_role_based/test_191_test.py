import unittest
from mbpp_191_code import check_monthnumber

class TestCheckMonthnumber(unittest.TestCase):
    def test_valid_months(self):
        self.assertTrue(check_monthnumber("April"))
        self.assertTrue(check_monthnumber("June"))
        self.assertTrue(check_monthnumber("September"))
        self.assertTrue(check_monthnumber("November"))

    def test_invalid_months(self):
        self.assertFalse(check_monthnumber("January"))
        self.assertFalse(check_monthnumber("February"))
        self.assertFalse(check_monthnumber("March"))
        self.assertFalse(check_monthnumber("May"))

    def test_case_insensitive(self):
        self.assertTrue(check_monthnumber("APRIL"))
        self.assertTrue(check_monthnumber("june"))
        self.assertTrue(check_monthnumber("september"))
        self.assertTrue(check_monthnumber("november"))
