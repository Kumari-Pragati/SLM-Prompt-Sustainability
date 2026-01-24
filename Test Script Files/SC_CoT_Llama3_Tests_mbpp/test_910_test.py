import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(check_date(1, 1, 2022))

    def test_valid_date_leap_year(self):
        self.assertTrue(check_date(2, 29, 2024))

    def test_invalid_date_month_zero(self):
        self.assertFalse(check_date(0, 1, 2022))

    def test_invalid_date_day_zero(self):
        self.assertFalse(check_date(1, 0, 2022))

    def test_invalid_date_day_greater_than_month(self):
        self.assertFalse(check_date(1, 32, 2022))

    def test_invalid_date_month_greater_than_12(self):
        self.assertFalse(check_date(13, 1, 2022))

    def test_invalid_date_year_zero(self):
        self.assertFalse(check_date(1, 1, 0))

    def test_invalid_date_year_negative(self):
        self.assertFalse(check_date(1, 1, -2022))

    def test_invalid_date_non_integer_input(self):
        with self.assertRaises(TypeError):
            check_date('a', 1, 2022)

    def test_invalid_date_non_integer_input_multiple(self):
        with self.assertRaises(TypeError):
            check_date('a', 'b', 2022)
