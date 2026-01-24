import unittest
from mbpp_928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_edge_case_single_digit_day(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_edge_case_single_digit_month(self):
        self.assertEqual(change_date_format('2022-1-01'), '01-01-2022')

    def test_boundary_case_end_of_year(self):
        self.assertEqual(change_date_format('2022-12-31'), '31-12-2022')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            change_date_format('2022-13-01')
