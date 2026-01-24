import unittest
from mbpp_191_code import check_monthnumber

class TestCheckMonthNumber(unittest.TestCase):

    def test_valid_months(self):
        """Test that valid months return True"""
        self.assertTrue(check_monthnumber("April"))
        self.assertTrue(check_monthnumber("June"))
        self.assertTrue(check_monthnumber("September"))
        self.assertTrue(check_monthnumber("November"))

    def test_invalid_months(self):
        """Test that invalid months return False"""
        self.assertFalse(check_monthnumber("January"))
        self.assertFalse(check_monthnumber("March"))
        self.assertFalse(check_monthnumber("December"))
        self.assertFalse(check_monthnumber("October"))

    def test_case_sensitivity(self):
        """Test that the function is case-insensitive"""
        self.assertTrue(check_monthnumber("april"))
        self.assertTrue(check_monthnumber("JUNE"))
        self.assertTrue(check_monthnumber("SEPTEMBER"))
        self.assertTrue(check_monthnumber("november"))

    def test_empty_string(self):
        """Test that an empty string returns False"""
        self.assertFalse(check_monthnumber(""))

    def test_non_string_input(self):
        """Test that non-string input raises a TypeError"""
        with self.assertRaises(TypeError):
            check_monthnumber(123)
