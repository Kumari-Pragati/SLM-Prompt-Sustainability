import unittest
from mbpp_928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):
    def test_valid_date_format(self):
        self.assertEqual(change_date_format('2022-07-25'), '25-07-2022')

    def test_valid_date_format_with_leading_zeros(self):
        self.assertEqual(change_date_format('2022-07-05'), '05-07-2022')

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            change_date_format('abc-def-ghi')

    def test_empty_string(self):
        self.assertEqual(change_date_format(''), '')

    def test_date_with_leading_zeros(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_date_with_trailing_zeros(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')
