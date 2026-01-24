import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(check_date(2, 29, 2020))
        self.assertTrue(check_date(12, 31, 2021))
        self.assertTrue(check_date(2, 28, 2021))

    def test_invalid_date_month(self):
        self.assertFalse(check_date(13, 1, 2021))
        self.assertFalse(check_date(0, 1, 2021))
        self.assertFalse(check_date(12, 32, 2021))

    def test_invalid_date_day(self):
        self.assertFalse(check_date(2, 32, 2021))
        self.assertFalse(check_date(2, 0, 2021))
        self.assertFalse(check_date(2, -1, 2021))

    def test_invalid_date_year(self):
        self.assertFalse(check_date(2, 29, 0))
        self.assertFalse(check_date(2, 29, 2000))
        self.assertFalse(check_date(2, 29, 2100))
