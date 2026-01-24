import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):
    def test_typical_use_case(self):
        url = 'https://example.com/2022/01/01/'
        self.assertEqual(extract_date(url), [('2022', '01', '01')])

    def test_edge_case(self):
        url = 'https://example.com/0000/01/01/'
        self.assertEqual(extract_date(url), [('0000', '01', '01')])

    def test_boundary_case(self):
        url = 'https://example.com/9999/12/31/'
        self.assertEqual(extract_date(url), [('9999', '12', '31')])

    def test_invalid_input(self):
        url = 'https://example.com/2022/13/01/'
        self.assertEqual(extract_date(url), [])
