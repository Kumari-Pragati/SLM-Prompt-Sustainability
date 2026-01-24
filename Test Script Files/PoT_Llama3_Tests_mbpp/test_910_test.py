import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(check_date(12, 25, 2022))

    def test_invalid_date(self):
        self.assertFalse(check_date(13, 25, 2022))

    def test_invalid_month(self):
        self.assertFalse(check_date(15, 25, 2022))

    def test_invalid_day(self):
        self.assertFalse(check_date(12, 30, 2022))

    def test_invalid_year(self):
        self.assertFalse(check_date(12, 25, 2020))

    def test_valid_date_with_leap_year(self):
        self.assertTrue(check_date(2, 29, 2024))

    def test_invalid_date_with_leap_year(self):
        self.assertFalse(check_date(2, 30, 2024))
