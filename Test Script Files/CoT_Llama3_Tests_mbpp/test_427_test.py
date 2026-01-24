import unittest
from mbpp_427_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):
    def test_typical_date(self):
        self.assertEqual(change_date_format('2022-07-25'), '25-07-2022')

    def test_edge_case_date(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_date_with_leading_zeros(self):
        self.assertEqual(change_date_format('2022-07-05'), '05-07-2022')

    def test_date_with_trailing_zeros(self):
        self.assertEqual(change_date_format('2022-07-25'), '25-07-2022')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            change_date_format('Invalid Date')

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            change_date_format('')
