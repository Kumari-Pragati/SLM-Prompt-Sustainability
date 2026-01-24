import unittest
from mbpp_928_code import datetime, timedelta
from 928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_simple_date(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_short_date(self):
        self.assertEqual(change_date_format('2022-1'), '01-1-2022')

    def test_long_date(self):
        self.assertEqual(change_date_format('2022-01-31 12:34:56'), '31-01-2022')

    def test_empty_string(self):
        self.assertEqual(change_date_format(''), '')

    def test_invalid_date(self):
        self.assertRaises(ValueError, change_date_format, '2022-32-01')

    def test_future_date(self):
        future_date = datetime.now() + timedelta(days=1)
        self.assertEqual(change_date_format(future_date.strftime('%Y-%m-%d')), future_date.strftime('%d-%m-%Y'))
