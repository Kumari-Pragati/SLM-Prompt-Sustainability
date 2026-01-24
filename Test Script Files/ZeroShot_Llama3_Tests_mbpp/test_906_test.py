import unittest
from mbpp_906_code import extract_date

class TestExtractDate(unittest.TestCase):

    def test_extract_date_valid_url(self):
        url = "https://example.com/2022/07/25/"
        self.assertEqual(extract_date(url), [('2022', '07', '25')])

    def test_extract_date_invalid_url(self):
        url = "https://example.com/invalid"
        self.assertEqual(extract_date(url), [])

    def test_extract_date_multiple_dates(self):
        url = "https://example.com/2022/07/25/2023/08/26/"
        self.assertEqual(extract_date(url), [('2022', '07', '25'), ('2023', '08', '26')])

    def test_extract_date_no_date(self):
        url = "https://example.com/no-date"
        self.assertEqual(extract_date(url), [])

    def test_extract_date_date_format(self):
        url = "https://example.com/2022/07/25/2023/08/26/2024/09/27/"
        self.assertEqual(extract_date(url), [('2022', '07', '25'), ('2023', '08', '26'), ('2024', '09', '27')])
