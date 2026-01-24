import unittest
from mbpp_928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):
    def test_valid_date_format(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')
        self.assertEqual(change_date_format('2022-01-31'), '31-01-2022')
        self.assertEqual(change_date_format('2022-12-31'), '31-12-2022')

    def test_short_month(self):
        self.assertEqual(change_date_format('2022-1-1'), '01-01-2022')
        self.assertEqual(change_date_format('2022-12-1'), '01-12-2022')

    def test_invalid_date_format(self):
        self.assertRaises(ValueError, change_date_format, 'invalid_date')
        self.assertRaises(ValueError, change_date_format, '2022-32-01')
        self.assertRaises(ValueError, change_date_format, '2022-00-01')
