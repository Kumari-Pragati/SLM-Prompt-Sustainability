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
        self.assertFalse(check_monthnumber("December"))
        self.assertFalse(check_monthnumber("March"))
        self.assertFalse(check_monthnumber("May"))
        self.assertFalse(check_monthnumber("July"))
        self.assertFalse(check_monthnumber("August"))
        self.assertFalse(check_monthnumber("October"))
