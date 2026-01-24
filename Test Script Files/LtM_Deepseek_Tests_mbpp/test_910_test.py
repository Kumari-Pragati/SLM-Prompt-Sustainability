import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):

    # Simple / typical inputs
    def test_typical_date(self):
        self.assertTrue(check_date(1, 1, 2000))

    # Edge and boundary conditions
    def test_minimum_date(self):
        self.assertTrue(check_date(1, 1, 1))

    def test_maximum_date(self):
        self.assertTrue(check_date(12, 31, 9999))

    def test_invalid_month(self):
        self.assertFalse(check_date(13, 1, 2000))

    def test_invalid_day(self):
        self.assertFalse(check_date(1, 31, 2000))

    # More complex or corner cases
    def test_leap_year(self):
        self.assertTrue(check_date(2, 29, 2000))

    def test_non_leap_year(self):
        self.assertFalse(check_date(2, 29, 2001))

    def test_invalid_year(self):
        self.assertFalse(check_date(1, 1, 10000))

    def test_invalid_input(self):
        self.assertFalse(check_date('a', 1, 2000))
        self.assertFalse(check_date(1, 'b', 2000))
        self.assertFalse(check_date(1, 1, 'c'))
