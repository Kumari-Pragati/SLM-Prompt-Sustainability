import unittest
from mbpp_427_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_simple_date(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_edge_case_month_less_than_10(self):
        self.assertEqual(change_date_format('2022-9-01'), '01-9-2022')

    def test_edge_case_month_greater_than_12(self):
        self.assertEqual(change_date_format('2022-13-01'), '01-13-2022')

    def test_edge_case_day_less_than_10(self):
        self.assertEqual(change_date_format('2022-01-9'), '09-01-2022')

    def test_edge_case_day_greater_than_31(self):
        self.assertEqual(change_date_format('2022-01-32'), '32-01-2022')

    def test_complex_date(self):
        self.assertEqual(change_date_format('2022-12-31'), '31-12-2022')
