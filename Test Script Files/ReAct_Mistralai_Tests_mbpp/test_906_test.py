import unittest
from mbpp_906_code import datetime, timedelta
from 906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_valid_date_format(self):
        self.assertListEqual(extract_date('/year/month/day/'), [('year', 'month', 'day')])

    def test_missing_year(self):
        self.assertListEqual(extract_date('/month/day/'), [None, 'month', 'day'])

    def test_missing_month(self):
        self.assertListEqual(extract_date('/year/day/'), [('year', None, None)])

    def test_missing_day(self):
        self.assertListEqual(extract_date('/year/month/'), [('year', 'month', None)])

    def test_invalid_year(self):
        self.assertListEqual(extract_date('/a/b/c/'), [None, None, None])

    def test_invalid_month(self):
        self.assertListEqual(extract_date('/year/a/c/'), [('year', None, None)])

    def test_invalid_day(self):
        self.assertListEqual(extract_date('/year/month/a/'), [('year', 'month', None)])

    def test_date_out_of_range(self):
        self.assertListEqual(extract_date('/2023/13/30/'), [('2023', None, None)])
        self.assertListEqual(extract_date('/2023/02/31/'), [('2023', '02', None)])
        self.assertListEqual(extract_date('/2023/12/32/'), [('2023', '12', None)])

    def test_date_with_leading_slash(self):
        self.assertListEqual(extract_date('/2023/01/01/'), [('2023', '01', '01')])

    def test_date_without_leading_slash(self):
        self.assertListEqual(extract_date('2023/01/01'), [('2023', '01', '01')])

    def test_date_with_trailing_slash(self):
        self.assertListEqual(extract_date('/2023/01/01/'), [('2023', '01', '01')])

    def test_date_with_multiple_slashes(self):
        self.assertListEqual(extract_date('/2023//01//01//'), [('2023', '01', '01')])

    def test_date_with_non_numeric_characters(self):
        self.assertListEqual(extract_date('/2023/a/b/'), [None, None, None])

    def test_date_with_non_numeric_year(self):
        self.assertListEqual(extract_date('/a/b/c/'), [None, None, None])

    def test_date_with_non_numeric_month(self):
        self.assertListEqual(extract_date('/2023/a/c/'), [('2023', None, None)])

    def test_date_with_non_numeric_day(self):
        self.assertListEqual(extract_date('/2023/12/a/'), [('2023', '12', None)])

    def test_date_with_empty_string(self):
        self.assertListEqual(extract_date(''), [])

    def test_date_with_multiple_dates(self):
        self.assertListEqual(extract_date('/2023/01/01/2022/12/31/'), [('2023', '01', '01'), ('2022', '12', '31')])

    def test_date_with_non_matching_format(self):
        self.assertListEqual(extract_date('/2023-01-01/'),