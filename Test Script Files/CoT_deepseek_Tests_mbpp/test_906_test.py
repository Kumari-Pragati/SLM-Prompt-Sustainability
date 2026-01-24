import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_typical_case(self):
        url = 'http://example.com/2022/01/01/'
        self.assertEqual(extract_date(url), [('2022', '01', '01')])

    def test_edge_case_single_digit_month(self):
        url = 'http://example.com/2022/1/01/'
        self.assertEqual(extract_date(url), [('2022', '1', '01')])

    def test_edge_case_single_digit_day(self):
        url = 'http://example.com/2022/01/1/'
        self.assertEqual(extract_date(url), [('2022', '01', '1')])

    def test_edge_case_single_digit_year(self):
        url = 'http://example.com/2022/01/01/'
        self.assertEqual(extract_date(url), [('2022', '01', '01')])

    def test_invalid_input(self):
        url = 'http://example.com/'
        self.assertEqual(extract_date(url), [])

    def test_invalid_date(self):
        url = 'http://example.com/2022/13/01/'
        self.assertEqual(extract_date(url), [])
