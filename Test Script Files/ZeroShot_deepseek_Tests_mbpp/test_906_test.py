import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_valid_url(self):
        self.assertEqual(extract_date('http://example.com/2022/01/01/'), [('2022', '01', '01')])
        self.assertEqual(extract_date('http://example.com/2021/12/31/'), [('2021', '12', '31')])

    def test_invalid_url(self):
        self.assertEqual(extract_date('http://example.com/2022/13/01/'), [])
        self.assertEqual(extract_date('http://example.com/2022/01/32/'), [])
        self.assertEqual(extract_date('http://example.com/2022/12/32/'), [])

    def test_missing_parts(self):
        self.assertEqual(extract_date('http://example.com/2022/01/'), [])
        self.assertEqual(extract_date('http://example.com/2022/'), [])
        self.assertEqual(extract_date('http://example.com/'), [])
