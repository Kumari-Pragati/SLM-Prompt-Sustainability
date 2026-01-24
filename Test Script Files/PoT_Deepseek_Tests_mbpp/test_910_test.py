import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_date(1, 1, 2022))

    def test_edge_case_january_1st_2000(self):
        self.assertTrue(check_date(1, 1, 2000))

    def test_boundary_case_end_of_month(self):
        self.assertTrue(check_date(12, 31, 2022))

    def test_invalid_month(self):
        self.assertFalse(check_date(13, 1, 2022))

    def test_invalid_day(self):
        self.assertFalse(check_date(1, 31, 2022))

    def test_invalid_year(self):
        self.assertFalse(check_date(1, 1, 0))

    def test_leap_year(self):
        self.assertTrue(check_date(2, 29, 2020))

    def test_non_leap_year(self):
        self.assertFalse(check_date(2, 29, 2021))

    def test_invalid_date(self):
        self.assertFalse(check_date(2, 30, 2021))
