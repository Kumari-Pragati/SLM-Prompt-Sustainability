import unittest
from mbpp_427_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_valid_date_format(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')
        self.assertEqual(change_date_format('2022-01-31'), '31-01-2022')
        self.assertEqual(change_date_format('2022-12-31'), '31-12-2022')

    def test_invalid_date_format_too_short(self):
        self.assertRaises(ValueError, change_date_format, '2022-')
        self.assertRaises(ValueError, change_date_format, '2022-01')
        self.assertRaises(ValueError, change_date_format, '2022-01-')

    def test_invalid_date_format_too_long(self):
        self.assertRaises(ValueError, change_date_format, '2022-01-01T12:00:00')
        self.assertRaises(ValueError, change_date_format, '2022-01-01Z')

    def test_invalid_date_format_non_numeric(self):
        self.assertRaises(ValueError, change_date_format, '2022-a-1')
        self.assertRaises(ValueError, change_date_format, '2022-1-a')
        self.assertRaises(ValueError, change_date_format, '2022-1-0a')
