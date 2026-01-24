import unittest
from mbpp_928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_edge_case_single_digit_day(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_edge_case_single_digit_month(self):
        self.assertEqual(change_date_format('2022-1-01'), '01-01-2022')

    def test_edge_case_leap_year(self):
        self.assertEqual(change_date_format('2024-02-29'), '29-02-2024')

    def test_error_case_invalid_date_format(self):
        with self.assertRaises(ValueError):
            change_date_format('2022-13-01')

    def test_error_case_invalid_date_value(self):
        with self.assertRaises(ValueError):
            change_date_format('2022-02-30')
