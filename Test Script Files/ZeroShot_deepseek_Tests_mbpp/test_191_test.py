import unittest
from mbpp_191_code import check_monthnumber

class TestCheckMonthNumber(unittest.TestCase):

    def test_valid_month(self):
        self.assertTrue(check_monthnumber("April"))
        self.assertTrue(check_monthnumber("June"))
        self.assertTrue(check_monthnumber("September"))
        self.assertTrue(check_monthnumber("November"))

    def test_invalid_month(self):
        self.assertFalse(check_monthnumber("January"))
        self.assertFalse(check_monthnumber("February"))
        self.assertFalse(check_monthnumber("December"))
        self.assertFalse(check_monthnumber("October"))
