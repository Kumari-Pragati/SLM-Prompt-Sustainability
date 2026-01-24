import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_typical_case(self):
        url = 'https://example.com/2023/04/15/'
        self.assertEqual(extract_date(url), [('2023', '04', '15')])

    def test_edge_case_single_digit_month(self):
        url = 'https://example.com/2023/4/15/'
        self.assertEqual(extract_date(url), [('2023', '04', '15')])

    def test_edge_case_single_digit_day(self):
        url = 'https://example.com/2023/04/5/'
        self.assertEqual(extract_date(url), [('2023', '04', '05')])

    def test_edge_case_single_digit_year(self):
        url = 'https://example.com/202/04/15/'
        self.assertEqual(extract_date(url), [('202', '04', '15')])

    def test_edge_case_missing_parts(self):
        url = 'https://example.com/2023/04/'
        self.assertEqual(extract_date(url), [])

    def test_edge_case_extra_parts(self):
        url = 'https://example.com/2023/04/15/extra'
        self.assertEqual(extract_date(url), [('2023', '04', '15')])

    def test_error_case_invalid_url(self):
        url = 'invalid_url'
        self.assertEqual(extract_date(url), [])
