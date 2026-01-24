import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(extract_date('https://example.com/2022/07/25/'), [('2022', '07', '25')])

    def test_edge_case_year(self):
        self.assertEqual(extract_date('https://example.com/1234/07/25/'), [('1234', '07', '25')])

    def test_edge_case_month(self):
        self.assertEqual(extract_date('https://example.com/2022/12/25/'), [('2022', '12', '25')])

    def test_edge_case_day(self):
        self.assertEqual(extract_date('https://example.com/2022/07/31/'), [('2022', '07', '31')])

    def test_edge_case_year_zero(self):
        self.assertEqual(extract_date('https://example.com/0001/07/25/'), [('0001', '07', '25')])

    def test_edge_case_month_zero(self):
        self.assertEqual(extract_date('https://example.com/2022/00/25/'), [])

    def test_edge_case_day_zero(self):
        self.assertEqual(extract_date('https://example.com/2022/07/00/'), [])

    def test_invalid_input(self):
        self.assertEqual(extract_date('https://example.com/'), [])
