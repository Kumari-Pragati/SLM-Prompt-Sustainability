import unittest
from mbpp_455_code import check_monthnumb_number

class TestCheckMonthnumbNumber(unittest.TestCase):

    def test_valid_months(self):
        """Test that valid months return True"""
        self.assertTrue(check_monthnumb_number(1))
        self.assertTrue(check_monthnumb_number(3))
        self.assertTrue(check_monthnumb_number(5))
        self.assertTrue(check_monthnumb_number(7))
        self.assertTrue(check_monthnumb_number(8))
        self.assertTrue(check_monthnumb_number(10))
        self.assertTrue(check_monthnumb_number(12))

    def test_invalid_months(self):
        """Test that invalid months return False"""
        self.assertFalse(check_monthnumb_number(0))
        self.assertFalse(check_monthnumb_number(2))
        self.assertFalse(check_monthnumb_number(4))
        self.assertFalse(check_monthnumb_number(6))
        self.assertFalse(check_monthnumb_number(9))
        self.assertFalse(check_monthnumb_number(11))
        self.assertFalse(check_monthnumb_number(13))

    def test_edge_cases(self):
        """Test edge cases of valid months"""
        self.assertTrue(check_monthnumb_number(12 if not self.is_leap_year() else 13))
        self.assertTrue(check_monthnumb_number(0 if not self.is_leap_year() else 1))

    def is_leap_year(self):
        """Helper function to check if a year is a leap year"""
        return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
