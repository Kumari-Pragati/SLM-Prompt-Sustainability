import unittest
from mbpp_427_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(change_date_format('2023-04-15'), '15-04-2023')

    def test_edge_case_single_digit_day(self):
        self.assertEqual(change_date_format('2023-04-01'), '01-04-2023')

    def test_edge_case_single_digit_month(self):
        self.assertEqual(change_date_format('2023-01-15'), '15-01-2023')

    def test_boundary_case_min_date(self):
        self.assertEqual(change_date_format('0001-01-01'), '01-01-0001')

    def test_boundary_case_max_date(self):
        self.assertEqual(change_date_format('9999-12-31'), '31-12-9999')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            change_date_format(123456)
