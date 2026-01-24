import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_date(1, 1, 2022))

    def test_typical_case_with_leap_year(self):
        self.assertTrue(check_date(2, 29, 2020))

    def test_typical_case_with_non_leap_year(self):
        self.assertFalse(check_date(2, 29, 2019))

    def test_invalid_day(self):
        self.assertFalse(check_date(1, 30, 2022))

    def test_invalid_month(self):
        self.assertFalse(check_date(13, 1, 2022))

    def test_invalid_year(self):
        self.assertFalse(check_date(1, 1, 0))

    def test_negative_day(self):
        self.assertFalse(check_date(1, -1, 2022))

    def test_negative_month(self):
        self.assertFalse(check_date(-1, 1, 2022))

    def test_negative_year(self):
        self.assertFalse(check_date(1, 1, -2022))

    def test_non_integer_day(self):
        self.assertFalse(check_date(1, 'a', 2022))

    def test_non_integer_month(self):
        self.assertFalse(check_date('b', 1, 2022))

    def test_non_integer_year(self):
        self.assertFalse(check_date(1, 1, 'c'))
