import unittest
from mbpp_191_code import months
from 191_code import check_monthnumber

class TestCheckMonthNumber(unittest.TestCase):
    def test_normal_case(self):
        self.assertTrue(check_monthnumber("April"))
        self.assertTrue(check_monthnumber("June"))
        self.assertTrue(check_monthnumber("September"))
        self.assertTrue(check_monthnumber("November"))

    def test_edge_case(self):
        self.assertFalse(check_monthnumber("March"))
        self.assertFalse(check_monthnumber("December"))
        self.assertFalse(check_monthnumber("January"))
        self.assertFalse(check_monthnumber("February"))
        self.assertFalse(check_monthnumber("October"))
        self.assertFalse(check_monthnumber("May"))
        self.assertFalse(check_monthnumber("July"))

    def test_invalid_input(self):
        self.assertFalse(check_monthnumber("Invalid Month"))
        self.assertFalse(check_monthnumber(123))
        self.assertFalse(check_monthnumber(months.december))
        self.assertFalse(check_monthnumber(None))
        self.assertFalse(check_monthnumber(""))
