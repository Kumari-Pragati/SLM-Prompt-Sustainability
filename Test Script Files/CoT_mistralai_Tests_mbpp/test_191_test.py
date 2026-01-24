import unittest
from mbpp_191_code import check_monthnumber

class TestCheckMonthNumber(unittest.TestCase):
    def test_valid_months(self):
        self.assertTrue(check_monthnumber("April"))
        self.assertTrue(check_monthnumber("June"))
        self.assertTrue(check_monthnumber("September"))
        self.assertTrue(check_monthnumber("November"))

    def test_invalid_months(self):
        self.assertFalse(check_monthnumber("January"))
        self.assertFalse(check_monthnumber("March"))
        self.assertFalse(check_monthnumber("December"))
        self.assertFalse(check_monthnumber("February"))
        self.assertFalse(check_monthnumber("May"))
        self.assertFalse(check_monthnumber("July"))
        self.assertFalse(check_monthnumber("October"))
        self.assertFalse(check_monthnumber("December31"))

    def test_invalid_input(self):
        self.assertRaises(TypeError, check_monthnumber, 123)
        self.assertRaises(TypeError, check_monthnumber, None)
        self.assertRaises(TypeError, check_monthnumber, [])
