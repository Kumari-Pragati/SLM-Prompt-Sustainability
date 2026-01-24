import unittest
from mbpp_427_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):
    def test_simple_date(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_short_date(self):
        self.assertEqual(change_date_format('2022-1'), '1-01-2022')
        self.assertEqual(change_date_format('2022-31'), '31-12-2022')

    def test_long_date(self):
        self.assertEqual(change_date_format('2022-01-01 12:34:56'), '01-01-2022')
        self.assertEqual(change_date_format('2022-01-01T12:34:56'), '01-01-2022')

    def test_empty_string(self):
        self.assertEqual(change_date_format(''), '')

    def test_invalid_date(self):
        self.assertRaises(ValueError, change_date_format, 'invalid-date')
