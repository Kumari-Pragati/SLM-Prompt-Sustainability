import unittest
from mbpp_928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):
    def test_typical_date(self):
        self.assertEqual(change_date_format('2022-07-25'), '25-07-2022')

    def test_date_with_leading_zeros(self):
        self.assertEqual(change_date_format('2022-07-05'), '05-07-2022')

    def test_date_with_trailing_zeros(self):
        self.assertEqual(change_date_format('2022-07-25'), '25-07-2022')

    def test_date_with_leading_and_trailing_zeros(self):
        self.assertEqual(change_date_format('2022-07-05'), '05-07-2022')

    def test_invalid_date_format(self):
        with self.assertRaises(TypeError):
            change_date_format('abc')

    def test_empty_string(self):
        self.assertEqual(change_date_format(''), '')

    def test_date_with_non_numeric_characters(self):
        with self.assertRaises(TypeError):
            change_date_format('2022-07-25abc')
