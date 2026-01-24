import unittest
from mbpp_928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(change_date_format('2022-07-25'), '25-07-2022')

    def test_empty_input(self):
        self.assertIsNone(change_date_format(''))

    def test_invalid_input(self):
        with self.assertRaises(re.error):
            change_date_format('Invalid date format')

    def test_date_format_with_leading_zeros(self):
        self.assertEqual(change_date_format('2022-07-05'), '05-07-2022')

    def test_date_format_with_trailing_zeros(self):
        self.assertEqual(change_date_format('2022-07-05'), '05-07-2022')

    def test_date_format_with_leading_and_trailing_zeros(self):
        self.assertEqual(change_date_format('2022-07-05'), '05-07-2022')

    def test_date_format_with_leading_zeros_and_spaces(self):
        self.assertEqual(change_date_format(' 2022-07-05'), '05-07-2022')

    def test_date_format_with_trailing_zeros_and_spaces(self):
        self.assertEqual(change_date_format('2022-07-05  '), '05-07-2022')

    def test_date_format_with_leading_and_trailing_zeros_and_spaces(self):
        self.assertEqual(change_date_format(' 2022-07-05  '), '05-07-2022')
