import unittest
from mbpp_427_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(change_date_format('2022-07-25'), '25-07-2022')

    def test_edge_case_year(self):
        self.assertEqual(change_date_format('2022-07-25-'), '25-07-2022')

    def test_edge_case_day(self):
        self.assertEqual(change_date_format('2022-07-'), '07-02-2022')

    def test_edge_case_month(self):
        self.assertEqual(change_date_format('2022-'), '02-02-2022')

    def test_edge_case_all(self):
        self.assertEqual(change_date_format(''), '')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            change_date_format('Invalid Date')

    def test_empty_string_input(self):
        self.assertEqual(change_date_format(''), '')

    def test_single_digit_day(self):
        self.assertEqual(change_date_format('2022-07-5'), '5-07-2022')

    def test_single_digit_month(self):
        self.assertEqual(change_date_format('2022-5-25'), '25-05-2022')

    def test_single_digit_year(self):
        self.assertEqual(change_date_format('5-07-25'), '25-07-05')
