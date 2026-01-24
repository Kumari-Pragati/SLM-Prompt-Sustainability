import unittest
from mbpp_191_code import check_monthnumber

class TestCheckMonthNumber(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(check_monthnumber("April"))
        self.assertTrue(check_monthnumber("June"))
        self.assertTrue(check_monthnumber("September"))
        self.assertTrue(check_monthnumber("November"))

    def test_edge_cases(self):
        self.assertFalse(check_monthnumber("January"))
        self.assertFalse(check_monthnumber("February"))
        self.assertFalse(check_monthnumber("March"))
        self.assertFalse(check_monthnumber("December"))
        self.assertFalse(check_monthnumber("May"))
        self.assertFalse(check_monthnumber("October"))
        self.assertFalse(check_monthnumber("December31"))

    def test_corner_cases(self):
        self.assertFalse(check_monthnumber(""))
        self.assertFalse(check_monthnumber(None))
        self.assertFalse(check_monthnumber("April_"))
        self.assertFalse(check_monthnumber("April "))
        self.assertFalse(check_monthnumber("April!"))
