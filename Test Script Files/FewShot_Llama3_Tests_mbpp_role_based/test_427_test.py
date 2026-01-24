import unittest
from mbpp_427_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):
    def test_typical_use_case(self):
        dt = '2022-07-25'
        expected_output = '25-07-2022'
        self.assertEqual(change_date_format(dt), expected_output)

    def test_edge_case_yyyy_mm_dd(self):
        dt = '2022-07-25'
        expected_output = '25-07-2022'
        self.assertEqual(change_date_format(dt), expected_output)

    def test_edge_case_dd_mm_yyyy(self):
        dt = '25-07-2022'
        expected_output = '25-07-2022'
        self.assertEqual(change_date_format(dt), expected_output)

    def test_edge_case_invalid_date(self):
        dt = 'abc-def-ghi'
        expected_output = dt
        self.assertEqual(change_date_format(dt), expected_output)

    def test_edge_case_empty_string(self):
        dt = ''
        expected_output = ''
        self.assertEqual(change_date_format(dt), expected_output)
