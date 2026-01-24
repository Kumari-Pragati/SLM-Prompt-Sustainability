import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_date('http://example.com/2022/01/01/'), [('2022', '01', '01')])

    def test_edge_case_single_digit_month(self):
        self.assertEqual(extract_date('http://example.com/2022/1/01/'), [('2022', '01', '01')])

    def test_edge_case_single_digit_day(self):
        self.assertEqual(extract_date('http://example.com/2022/01/1/'), [('2022', '01', '01')])

    def test_edge_case_leap_year(self):
        self.assertEqual(extract_date('http://example.com/2024/02/29/'), [('2024', '02', '29')])

    def test_corner_case_invalid_date(self):
        self.assertEqual(extract_date('http://example.com/2022/13/01/'), [])

    def test_corner_case_invalid_url(self):
        self.assertEqual(extract_date('http://example.com/2022/01/01'), [])
