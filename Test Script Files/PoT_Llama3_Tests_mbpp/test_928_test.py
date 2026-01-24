import unittest
from mbpp_928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):
    def test_typical_date(self):
        self.assertEqual(change_date_format('2022-07-25'), '25-07-2022')

    def test_typical_date_with_leading_zeros(self):
        self.assertEqual(change_date_format('2022-07-05'), '05-07-2022')

    def test_edge_case_date(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_edge_case_date_with_leading_zeros(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            change_date_format('abc')

    def test_invalid_date_with_leading_zeros(self):
        with self.assertRaises(ValueError):
            change_date_format('abc')
