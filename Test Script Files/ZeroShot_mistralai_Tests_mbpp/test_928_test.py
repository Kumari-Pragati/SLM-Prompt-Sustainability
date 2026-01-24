import unittest
from mbpp_928_code import datetime, date
from 928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(change_date_format(''), '')

    def test_invalid_date_format(self):
        self.assertRaises(ValueError, change_date_format, 'invalid_date')

    def test_date_format_1(self):
        self.assertEqual(change_date_format('2022-12-31'), '31-12-2022')

    def test_date_format_2(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_date_format_3(self):
        self.assertEqual(change_date_format('2022-02-28'), '28-02-2022')

    def test_date_format_4(self):
        self.assertEqual(change_date_format('2022-02-29'), '29-02-2022')

    def test_date_format_5(self):
        self.assertEqual(change_date_format('2022-03-01'), '01-03-2022')

    def test_date_object_1(self):
        dt = datetime(2022, 12, 31)
        self.assertEqual(change_date_format(dt.strftime('%Y-%m-%d')), '31-12-2022')

    def test_date_object_2(self):
        dt = date(2022, 1, 1)
        self.assertEqual(change_date_format(dt.strftime('%Y-%m-%d')), '01-01-2022')
