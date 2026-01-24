import unittest
from mbpp_427_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_edge_case_day(self):
        self.assertEqual(change_date_format('2022-01-00'), '00-01-2022')

    def test_edge_case_month(self):
        self.assertEqual(change_date_format('2022-00-01'), '01-00-2022')

    def test_edge_case_year(self):
        self.assertEqual(change_date_format('0000-01-01'), '01-01-0000')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            change_date_format(123456)
