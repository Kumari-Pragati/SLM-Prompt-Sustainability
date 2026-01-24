import unittest
from mbpp_191_code import check_monthnumber

class TestCheckMonthNumber(unittest.TestCase):
    def test_april(self):
        self.assertTrue(check_monthnumber("April"))

    def test_june(self):
        self.assertTrue(check_monthnumber("June"))

    def test_september(self):
        self.assertTrue(check_monthnumber("September"))

    def test_november(self):
        self.assertTrue(check_monthnumber("November"))

    def test_invalid_month(self):
        self.assertFalse(check_monthnumber("January"))

    def test_non_string_input(self):
        self.assertRaises(TypeError, check_monthnumber, 123)

    def test_empty_string(self):
        self.assertFalse(check_monthnumber(""))
