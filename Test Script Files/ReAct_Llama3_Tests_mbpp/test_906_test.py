import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_typical_url(self):
        url = 'https://example.com/2022/07/25/'
        self.assertEqual(extract_date(url), [('2022', '07', '25')])

    def test_edge_case_url(self):
        url = 'https://example.com/2022/07/01/'
        self.assertEqual(extract_date(url), [('2022', '07', '01')])

    def test_multiple_matches_url(self):
        url = 'https://example.com/2022/07/25/2022/08/01/'
        self.assertEqual(extract_date(url), [('2022', '07', '25'), ('2022', '08', '01')])

    def test_no_matches_url(self):
        url = 'https://example.com/no-date-in-url/'
        self.assertEqual(extract_date(url), [])

    def test_invalid_url(self):
        url = 'https://example.com/invalid-date-format/'
        with self.assertRaises(re.error):
            extract_date(url)

    def test_empty_url(self):
        url = ''
        self.assertEqual(extract_date(url), [])
