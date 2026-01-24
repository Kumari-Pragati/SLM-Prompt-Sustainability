import unittest
from mbpp_191_code import check_monthnumber

class TestCheckMonthNumber(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(check_monthnumber("April"))
        self.assertTrue(check_monthnumber("June"))
        self.assertTrue(check_monthnumber("September"))
        self.assertTrue(check_monthnumber("November"))

    def test_edge_cases(self):
        self.assertFalse(check_monthnumber(""))
        self.assertFalse(check_monthnumber(" "))
        self.assertFalse(check_monthnumber("InvalidMonth"))

    def test_boundary_conditions(self):
        self.assertFalse(check_monthnumber("A"))
        self.assertFalse(check_monthnumber("J"))
        self.assertFalse(check_monthnumber("JU"))
        self.assertFalse(check_monthnumber("JUN"))
        self.assertFalse(check_monthnumber("JUNES"))
        self.assertFalse(check_monthnumber("JUNESS"))
        self.assertFalse(check_monthnumber("JUNESST"))
        self.assertFalse(check_monthnumber("JUNESTT"))
