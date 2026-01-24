import unittest
from mbpp_191_code import check_monthnumber

class TestCheckMonthNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_monthnumber("April"))
        self.assertTrue(check_monthnumber("June"))
        self.assertTrue(check_monthnumber("September"))
        self.assertTrue(check_monthnumber("November"))
        self.assertFalse(check_monthnumber("January"))
        self.assertFalse(check_monthnumber("December"))

    def test_edge_cases(self):
        self.assertFalse(check_monthnumber(""))
        self.assertFalse(check_monthnumber(" " * 100))
        self.assertFalse(check_monthnumber("InvalidMonth"))

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            check_monthnumber(123)
        with self.assertRaises(TypeError):
            check_monthnumber(None)
